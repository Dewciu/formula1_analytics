import pandas as pd
from formula1_analytics.common.protocols.data import Data
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.drivers.drivers import Drivers, DriversColumns


class DriversMostWins:
    # TODO - add driver names
    results: Data = Results()
    drivers: Data = Drivers()
    _data: pd.DataFrame

    def __init__(self, count: int) -> None:
        self._count = count

    def get_data(self) -> pd.DataFrame:
        """
        Description
        -----------
        Get the most successful drivers in terms of wins.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the most successful drivers in terms of wins.

        DataFrame columns:
            - driverId: int64
            - wins: int64
        """

        self._get_driver_position_results()
        self._get_first_pos_results()
        self._get_first_pos_counts_for_each_driver()
        self._rename_position_col_to_wins()
        self._sort_by_wins()

        return self._data.head(self._count)

    def _get_driver_position_results(self) -> None:
        self._data = self.results.get_selected_columns(
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POSITION,
        )

    def _get_first_pos_results(self) -> None:
        self._data = self._data[self._data[ResultsColumns.POSITION] == 1]

    def _get_first_pos_counts_for_each_driver(self) -> None:
        self._data = self._data.groupby(ResultsColumns.DRIVER_ID).count()

    def _rename_position_col_to_wins(self) -> None:
        self._data.rename(columns={ResultsColumns.POSITION: "wins"}, inplace=True)

    def _sort_by_wins(self) -> None:
        self._data = self._data.sort_values("wins", ascending=False)

    def _add_driver_names(self, win_counts: pd.DataFrame) -> pd.DataFrame:
        ...

    def _get_driver_names(self, driver_ids: pd.Series) -> pd.Series:
        return (
            self.drivers.get_selected_columns(
                DriversColumns.DRIVER_ID,
                DriversColumns.FORENAME,
                DriversColumns.SURNAME,
            )
            .set_index(DriversColumns.DRIVER_ID)
            .loc[driver_ids]
        )
