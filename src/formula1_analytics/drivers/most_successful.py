import pandas as pd
from formula1_analytics.results.results import Results


class MostSuccessful:
    results = Results()

    def get(self, count: int) -> pd.DataFrame:
        ...

    def _process_results(self) -> pd.DataFrame:
        ...

    def _get_most_wins(self) -> pd.DataFrame:
        ...

    def _get_specified_results(self) -> pd.DataFrame:
        self.results.get_selected_columns("")
