import pandas as pd
from pathlib import Path
from config.config import RAW_DATA_PATH


class DataLoader:
    def __init__(self, filename: str) -> None:
        self.path = Path(RAW_DATA_PATH).joinpath(filename)
        print(self.path)

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.path)
