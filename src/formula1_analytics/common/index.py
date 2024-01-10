import pandas as pd


class Index:
    @staticmethod
    def id_to_index(df: pd.DataFrame, id_col: str) -> pd.DataFrame:
        """
        Convert id column to index column
        """
        df.index = df[id_col]
        df.drop(id_col, axis=1, inplace=True)
        return df
