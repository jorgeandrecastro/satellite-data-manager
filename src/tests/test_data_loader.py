import pandas as pd

from src.data_loader import DataLoader


def test_load_csv(tmp_path):
    # Crée un CSV temporaire
    file = tmp_path / "test.csv"
    df_input = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df_input.to_csv(file, index=False)

    # Test du chargement
    loader = DataLoader(tmp_path)
    df = loader.load_csv("test.csv")

    assert df.shape == (2, 2)
    assert list(df.columns) == ["a", "b"]
