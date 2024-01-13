import pandas as pd
from formula1_analytics.logger import get_logger
from formula1_analytics.drivers.drivers import Drivers, DriversColumns
from formula1_analytics.races.races import Races, RacesColumns
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.drivers.exceptions import (
    SeasonNotFoundException,
    DriverNotFoundException,
    InvalidSeasonException,
)

LOGGER = get_logger(__name__)


class DriversSeasonPerfColumns:
    ROUND = "round"
    DRIVER_FULLNAME = "driver_fullname"
    TOTAL_POINTS = "total_points"


class DriversSeasonPerf:
    _data: pd.DataFrame

    def __init__(self) -> None:
        LOGGER.debug("Initializing DriversSeasonPerf class")
        self._drivers = Drivers().get_driver_fullnames()
        LOGGER.debug(f"Got drivers: \n {self._drivers}")
        self._races = Races().get_selected_columns(
            RacesColumns.YEAR,
            RacesColumns.ROUND,
        )
        LOGGER.debug(f"Got races: \n {self._races}")
        self._results = Results().get_selected_columns(
            ResultsColumns.RACE_ID,
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POINTS,
        )
        LOGGER.debug(f"Got results: \n {self._results}")

    def get_data(
        self,
        season_year: int,
        driver_names: list[str],
    ) -> pd.DataFrame:
        """
        Description
        -----------
        Get the performance of each driver in a given season.

        Parameters
        ----------
        season : int
            The season to get the performance for (1996-2023).
        drivers : list[str], optional
            A list of driver names to filter the results by, by default None.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the performance of each driver in a given season.
        """
        if not isinstance(season_year, int):
            raise TypeError("Season year must be an integer")
        if season_year < 1996 or season_year > 2023:
            raise InvalidSeasonException(season_year, range(1996, 2024))

        self._attach_driver_fullname_to_results()
        self._set_races_for_selected_season(season_year)
        self._attach_race_round_to_results()
        self._transform_drivers_to_columns()
        self._add_first_zero_row()
        self._cumulative_sum_points_for_each_driver()
        if driver_names:
            if not isinstance(driver_names, list):
                raise TypeError("Driver names must be a list")
            self._filter_drivers(driver_names)
        return self._results

    def _attach_driver_fullname_to_results(self) -> None:
        LOGGER.debug("Attaching driver fullname to results...")
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
        LOGGER.debug(f"Driver fullname attached to results: \n {self._results}")

    def _set_races_for_selected_season(self, season_year: int) -> None:
        LOGGER.debug(f"Filtering races by season year... {season_year}")
        self._races = self._races[self._races[RacesColumns.YEAR] == season_year]
        if self._races.empty:
            raise SeasonNotFoundException(season_year)
        LOGGER.debug(f"Races filtered by season year: {self._races}")

    def _attach_race_round_to_results(self) -> None:
        LOGGER.debug("Attaching race round to results, and dropping race ID column...")
        self._results = self._results.merge(
            self._races[RacesColumns.ROUND],
            left_on=ResultsColumns.RACE_ID,
            right_on=RacesColumns.RACE_ID,
        ).drop(columns=[ResultsColumns.RACE_ID])
        LOGGER.debug(f"Results with attached race round: \n {self._results}")

    def _transform_drivers_to_columns(self) -> None:
        LOGGER.debug("Transforming driver names to columns...")
        self._results = self._results.pivot(
            index=DriversSeasonPerfColumns.ROUND,
            columns=DriversSeasonPerfColumns.DRIVER_FULLNAME,
            values=ResultsColumns.POINTS,
        )
        LOGGER.debug(f"Results with driver names as columns: \n {self._results}")

    def _cumulative_sum_points_for_each_driver(self) -> None:
        LOGGER.debug("Calculating cumulative sum of points for each driver...")
        self._results = self._results.cumsum().fillna(method="ffill")
        LOGGER.debug(f"Results with cumulative sum of points: \n {self._results}")

    def _add_first_zero_row(self) -> None:
        LOGGER.debug("Adding first row of zeros...")
        self._results.loc[0] = [0 for _ in range(len(self._results.columns))]
        self._results.sort_index(inplace=True)
        LOGGER.debug(f"Results with first row of zeros: \n {self._results}")

    def _filter_drivers(self, drivers: list[str]) -> None:
        LOGGER.debug(f"Filtering drivers by: {drivers}")
        for driver in drivers:
            if driver not in self._results.columns:
                raise DriverNotFoundException(driver)

        self._results = self._results[list(drivers)]
        LOGGER.debug(f"Results filtered by drivers: \n {self._results}")
