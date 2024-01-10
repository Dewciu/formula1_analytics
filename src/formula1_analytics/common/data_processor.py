import pandas as pd
import numpy as np


class DataProcessor:
    @staticmethod
    def empty_to_nan(df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert "N" strings to NaN
        """
        return df.replace(r"\\N", np.NaN, regex=True, inplace=True)

    @staticmethod
    def merge(axis: int = 1, *data: pd.DataFrame | pd.Series) -> pd.DataFrame:
        """
        Merge dataframes or series
        """
        return pd.concat(data, axis=axis)
