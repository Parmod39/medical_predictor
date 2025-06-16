from .data_loader import DataLoader
from pywebio import start_server
from pywebio.input import actions
from pywebio.output import put_text, put_markdown, put_loading, clear, style
from time import sleep

class DiseasePredictorApp:
    """
    The main application class.
    Uses a predictor strategy to interactively query symptoms and predict diseases.
    """
    def __init__(self, strategy_cls, dataset_file: str = r'C:\Users\Parmod Budhiraja\OneDrive\Desktop\coding\Training.csv'):
        self._dataset_file = dataset_file
        self._strategy_cls = strategy_cls
        self._strategy = None
        self._asked = set()

    def _load_data(self):
        loader = DataLoader(self._dataset_file)
        return loader.load()

    def run(self):
        put_markdown("# Disease Predictor from Symptoms")
        put_text("This application uses a decision tree algorithm to predict a possible disease based on your symptoms.")
        put_markdown("---")

        try:
            df = self._load_data()
        except FileNotFoundError as e:
            clear()
            put_markdown("## Error: Dataset Not Found")
            style(put_text(str(e)), 'color:red')
            return

        with put_loading():
            sleep(1)

        clear()
        self._strategy = self._strategy_cls(df)
        self._interactive_loop()
        self._display_result()

    def _interactive_loop(self):
        while self._strategy._df['Disease'].nunique() > 1:
            symptom = self._strategy.next_symptom(self._asked)
            if not symptom:
                break
            clear()
            put_markdown("# Disease Predictor")
            put_markdown(f"Do you have the symptom: *{symptom.capitalize()}*?")
            response = actions(buttons=['Yes', 'No'])
            if response is None:
                put_text("Session closed by user.")
                return
            self._strategy.filter_data(symptom, response == 'Yes')
            self._asked.add(symptom)
            if self._strategy._df.empty:
                break

    def _display_result(self):
        clear()
        put_markdown("# Prediction Result")
        df = self._strategy._df
        if df.empty:
            put_markdown("### No Matching Disease Found")
            put_text("No disease matches your symptom combination. Consult a professional.")
        elif df['Disease'].nunique() == 1:
            disease = df['Disease'].iloc[0]
            put_markdown(f"## Predicted Disease: *{disease}*")
            put_markdown("---")
            put_text("Disclaimer: Not a substitute for professional medical advice.")
        else:
            put_markdown("### Could Not Determine a Single Disease")
            put_text("Possible conditions based on your answers:")
            for d in sorted(df['Disease'].unique()):
                put_text(f"- {d}")
            put_markdown("\n*Consult a professional for accurate diagnosis.*")