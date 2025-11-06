from pathlib import Path

import pandas as pd


class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_csv(self, filename: str) -> pd.DataFrame:
        path = self.data_path / filename
        if not path.exists():
            raise FileNotFoundError(f"{filename} not found in {self.data_path}")
        df = pd.read_csv(path)
        print(f"{filename} loaded, shape: {df.shape}")
        return df
