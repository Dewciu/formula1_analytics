import pandas as pd


class DataProcessor:
    @staticmethod
    def empty_to_nan(df: pd.DataFrame) -> None:
        """
        Convert "N" strings to NaN
        """
        df.replace(r"\\N", pd.NA, regex=True, inplace=True)

    @staticmethod
    def convert_types(
        df: pd.DataFrame,
        column_types: dict[str, str],
    ) -> None:
        """
        Convert numeric columns to numeric
        """
        for column, dtype in column_types.items():
            try:
                df[column] = df[column].astype(dtype)
            except TypeError:
                print(f"Cannot convert {column} to {dtype}")

    @staticmethod
    def merge(axis: int = 1, *data: pd.DataFrame | pd.Series) -> pd.DataFrame:
        """
        Merge dataframes or series
        """
        return pd.concat(data, axis=axis)
