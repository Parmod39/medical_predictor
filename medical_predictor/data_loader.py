import os
import pandas as pd

class DataLoader:
    """
    Handles loading and preprocessing of the dataset.
    Encapsulates file operations and data cleaning.
    """
    def __init__(self, filename: str):
        self._filename = filename
        self._df = None

    def load(self) -> pd.DataFrame:
        if not os.path.exists(self._filename):
            raise FileNotFoundError(f"Dataset '{self._filename}' not found.")

        df = pd.read_csv(self._filename)
        df.columns = df.columns.str.strip()
        if 'Prognosis' in df.columns:
            df.rename(columns={'Prognosis': 'Disease'}, inplace=True)
        else:
            df.rename(columns={df.columns[0]: 'Disease'}, inplace=True)
        self._df = df
        return self._df