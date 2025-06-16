from abc import ABC, abstractmethod
import numpy as np

class PredictorStrategy(ABC):
    """
    Abstract base class for predictor strategies.
    Defines interface for asking symptoms and filtering data.
    """
    def __init__(self, df):
        self._df = df.copy()

    @abstractmethod
    def next_symptom(self, asked: set) -> str:
        """
        Selects the next best symptom to ask based on strategy.
        """
        pass

    def filter_data(self, symptom: str, has: bool):
        mask = self._df.iloc[:, 1:].apply(
            lambda row: symptom in [str(s).replace('_', ' ').strip() for s in row.values],
            axis=1
        )
        self._df = self._df[mask] if has else self._df[~mask]

    @staticmethod
    def _calculate_entropy(series) -> float:
        counts = series.value_counts()
        probs = counts / counts.sum()
        return -np.sum(probs * np.log2(probs)) if len(probs) > 1 else 0.0

    def _information_gain(self, symptom: str) -> float:
        parent_entropy = self._calculate_entropy(self._df['Disease'])
        mask = self._df.iloc[:, 1:].apply(
            lambda row: symptom in [str(s).replace('_', ' ').strip() for s in row.values],
            axis=1
        )
        df_yes = self._df[mask]
        df_no = self._df[~mask]
        if df_yes.empty or df_no.empty:
            return 0.0
        weight_yes = len(df_yes) / len(self._df)
        child_entropy = (
            weight_yes * self._calculate_entropy(df_yes['Disease']) +
            (1 - weight_yes) * self._calculate_entropy(df_no['Disease'])
        )
        return parent_entropy - child_entropy