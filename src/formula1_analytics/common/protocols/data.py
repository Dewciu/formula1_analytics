from typing import Protocol
import pandas as pd


class Data(Protocol):
    def get_data(self) -> pd.DataFrame:
        ...
