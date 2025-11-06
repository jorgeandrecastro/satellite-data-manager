import pandas as pd


class DataCleaner:
    @staticmethod
    def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna()

    @staticmethod
    def lowercase_columns(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [col.lower() for col in df.columns]
        return df

    @staticmethod
    def normalize_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
        if col not in df.columns:
            raise ValueError(f"{col} not in dataframe")
        df[col] = (df[col] - df[col].mean()) / df[col].std()
        return df
