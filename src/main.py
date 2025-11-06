import asyncio

from data_cleaner import DataCleaner
from data_loader import DataLoader


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        result = func(*args, **kwargs)
        print(
            f"Résultat: {result if isinstance(result, (int,float,str)) else type(result)}"
        )
        return result

    return wrapper


class SatelliteManager:
    def __init__(self, data_path: str):
        self.loader = DataLoader(data_path)
        self.cleaner = DataCleaner()

    @log_function
    async def process_csv(self, filename: str):
        df = self.loader.load_csv(filename)
        df = self.cleaner.drop_missing(df)
        df = self.cleaner.lowercase_columns(df)
        if 'altitude' in df.columns:
            df = self.cleaner.normalize_column(df, 'altitude')
        print(df.head())
        return df


async def main():
    manager = SatelliteManager(data_path="./data")
    await manager.process_csv("satellite_demo.csv")


if __name__ == "__main__":
    asyncio.run(main())
