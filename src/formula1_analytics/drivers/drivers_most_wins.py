import pandas as pd
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.drivers.drivers import Drivers


class DriversMostWins:
    # TODO - add driver names
    _results = Results()
    _drivers = Drivers()
    _data: pd.DataFrame

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
        self._data = self._results.get_selected_columns(
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

    def _add_drivers_fullnames(self) -> None:
        self._data = pd.merge(
            self._data,
            self._drivers.get_driver_fullnames(),
            left_index=True,
            right_index=True,
        )
