import pandas as pd
from formula1_analytics.common.data_loader import DataLoader
from formula1_analytics.common.index_manager import IndexManager
from formula1_analytics.common.data_processor import DataProcessor


class F1Data:
    _data: pd.DataFrame

    def __init__(
        self,
        filename: str,
        id_name: str,
    ) -> None:
        self._data = DataLoader().load_data(filename)
        if id_name is not None:
            IndexManager.id_to_index(self._data, id_name)
        else:
            self._data["index"] = self._data.index
        
        DataProcessor.empty_to_nan(self._data)

    def get_data(self) -> pd.DataFrame:
        return self._data

    def get_selected_columns(
        self,
        *args,
    ) -> pd.DataFrame:
        return self._data[list(args)]
