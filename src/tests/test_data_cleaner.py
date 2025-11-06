import pandas as pd

from src.data_cleaner import DataCleaner


def test_lowercase_columns():
    df = pd.DataFrame({"A": [1], "B": [2]})
    df = DataCleaner.lowercase_columns(df)
    assert list(df.columns) == ["a", "b"]
