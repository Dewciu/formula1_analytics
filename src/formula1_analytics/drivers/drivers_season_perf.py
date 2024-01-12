import pandas as pd
from formula1_analytics.drivers.drivers import Drivers, DriversColumns
from formula1_analytics.races.races import Races, RacesColumns
from formula1_analytics.results.results import Results, ResultsColumns


class DriversSeasonPerfColumns:
    ROUND = "round"
    DRIVER_FULLNAME = "driver_fullname"
    TOTAL_POINTS = "total_points"


class DriversSeasonPerf:
    _drivers = Drivers().get_driver_fullnames()
    _races = Races().get_selected_columns(
        RacesColumns.YEAR,
        RacesColumns.ROUND,
    )
    _results = Results().get_selected_columns(
        ResultsColumns.RACE_ID,
        ResultsColumns.DRIVER_ID,
        ResultsColumns.POINTS,
    )
    _data: pd.DataFrame

    def get_data(
        self,
        season_year: int,
        *driver_names: str,
    ) -> pd.DataFrame:
        """
        Description
        -----------
        Get the performance of each driver in a given season.

        Parameters
        ----------
        season : int
            The season to get the performance for.
        drivers : list[str], optional
            A list of driver names to filter the results by, by default None.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the performance of each driver in a given season.
        """

        self._attach_driver_fullname_to_results()
        self._set_races_for_selected_season(season_year)
        self._attach_race_round_to_results()
        self._transform_drivers_to_columns()
        self._add_first_zero_row()
        self._cumulative_sum_points_for_each_driver()
        if driver_names:
            self._filter_drivers(driver_names)
        return self._results

    def _attach_driver_fullname_to_results(self) -> None:
        self._results = (
            self._results.merge(
                self._drivers,
                left_on=ResultsColumns.DRIVER_ID,
                right_on=DriversColumns.DRIVER_ID,
            )
            .rename(
                columns={DriversColumns.FULLNAME: "driver_fullname"},
            )
            .drop(
                columns=[DriversColumns.DRIVER_ID],
            )
        )

    def _set_races_for_selected_season(self, season_year: int) -> None:
        self._races = self._races[self._races[RacesColumns.YEAR] == season_year]
        if self._races.empty:
            raise ValueError(f"Season {season_year} not found.")

    def _attach_race_round_to_results(self) -> None:
        self._results = self._results.merge(
            self._races[RacesColumns.ROUND],
            left_on=ResultsColumns.RACE_ID,
            right_on=RacesColumns.RACE_ID,
        ).drop(columns=[ResultsColumns.RACE_ID])

    def _transform_drivers_to_columns(self) -> None:
        self._results = self._results.pivot(
            index=DriversSeasonPerfColumns.ROUND,
            columns=DriversSeasonPerfColumns.DRIVER_FULLNAME,
            values=ResultsColumns.POINTS,
        )

    def _cumulative_sum_points_for_each_driver(self) -> None:
        self._results = self._results.cumsum().fillna(method="ffill")

    def _add_first_zero_row(self) -> None:
        self._results.loc[0] = [0 for _ in range(len(self._results.columns))]
        self._results.sort_index(inplace=True)

    def _filter_drivers(self, drivers: list[str]) -> None:
        for driver in drivers:
            if driver not in self._results.columns:
                raise ValueError(
                    f"Driver {driver} not found. List all drivers with `Drivers().get_driver_fullnames()`."
                )

        self._results = self._results[list(drivers)]
