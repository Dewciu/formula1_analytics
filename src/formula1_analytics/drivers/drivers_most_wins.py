import pandas as pd
from formula1_analytics.logger import get_logger
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.drivers.drivers import Drivers

LOGGER = get_logger(__name__)


class DriversMostWins:
    _data: pd.DataFrame

    def __init__(self) -> None:
        self._results = Results()
        self._drivers = Drivers()

    def get_data(self, count: int) -> pd.DataFrame:
        """
        Description
        -----------
        Get the most successful drivers in terms of wins.

        Parameters
        ----------
        count : int
            The number of top drivers to return.

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
        self._add_drivers_fullnames()

        return self._data.head(count)

    def _get_driver_position_results(self) -> None:
        LOGGER.debug("Getting driver position results...")
        self._data = self._results.get_selected_columns(
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POSITION,
        )
        LOGGER.debug(f"Got driver position results: \n {self._data}")

    def _get_first_pos_results(self) -> None:
        LOGGER.debug("Getting first position results...")
        self._data = self._data[self._data[ResultsColumns.POSITION] == 1]
        LOGGER.debug(f"Got first position results: \n {self._data}")

    def _get_first_pos_counts_for_each_driver(self) -> None:
        LOGGER.debug("Getting first position counts for each driver...")
        self._data = self._data.groupby(ResultsColumns.DRIVER_ID).count()
        LOGGER.debug(f"Got first position counts for each driver: \n {self._data}")

    def _rename_position_col_to_wins(self) -> None:
        LOGGER.debug("Renaming position column to wins...")
        self._data.rename(columns={ResultsColumns.POSITION: "wins"}, inplace=True)
        LOGGER.debug(f"Renamed position column to wins: \n {self._data}")

    def _sort_by_wins(self) -> None:
        LOGGER.debug("Sorting by wins...")
        self._data = self._data.sort_values("wins", ascending=False)
        LOGGER.debug(f"Sorted by wins: \n {self._data}")

    def _add_drivers_fullnames(self) -> None:
        LOGGER.debug("Adding drivers fullnames...")
        self._data = pd.merge(
            self._data,
            self._drivers.get_driver_fullnames(),
            left_index=True,
            right_index=True,
        )
        LOGGER.debug(f"Added drivers fullnames: \n {self._data}")
