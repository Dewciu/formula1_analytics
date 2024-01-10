import pandas as pd
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.drivers.drivers import Drivers, DriversColumns


class MostSuccessful:
    # TODO - try to do this as a pipeline
    # TODO - add driver names

    results = Results()
    drivers = Drivers()
    _data: pd.DataFrame

    def get(
        self,
        count: int,
    ) -> pd.DataFrame:
        drivers_pos_results = self._get_driver_position_results()
        drivers_wins_counts = self._get_wins_counts_for_each_driver(drivers_pos_results)
        return self._sort_by_wins(drivers_wins_counts).head(count)

    def _get_driver_position_results(self) -> pd.DataFrame:
        return self.results.get_selected_columns(
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POSITION,
        )

    def _get_wins_counts_for_each_driver(
        self,
        driver_pos_results: pd.DataFrame,
    ) -> pd.DataFrame:
        first_pos_results = driver_pos_results[
            driver_pos_results[ResultsColumns.POSITION] == 1
        ]
        first_post_counts = first_pos_results.groupby(ResultsColumns.DRIVER_ID).count()
        first_post_counts.rename(
            columns={ResultsColumns.POSITION: "wins"}, inplace=True
        )

        return first_post_counts

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

    @staticmethod
    def _sort_by_wins(win_counts: pd.DataFrame) -> pd.DataFrame:
        return win_counts.sort_values("wins", ascending=False)
