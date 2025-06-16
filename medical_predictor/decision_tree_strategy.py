from .predictor_strategy import PredictorStrategy

class DecisionTreeStrategy(PredictorStrategy):
    """
    Implements a decision tree approach using entropy and information gain.
    """
    def next_symptom(self, asked: set) -> str:
        all_symptoms = set(self._df.iloc[:, 1:].stack().dropna().unique())
        all_symptoms = {s.replace('_', ' ').strip() for s in all_symptoms}
        candidates = all_symptoms - asked
        best, best_ig = None, 0.0
        for symptom in candidates:
            ig = self._information_gain(symptom)
            if ig > best_ig:
                best_ig = ig
                best = symptom
        return best if best_ig > 0 else None