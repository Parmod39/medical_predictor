from medical_predictor.decision_tree_strategy import DecisionTreeStrategy
from medical_predictor.app import DiseasePredictorApp
from pywebio import start_server

if __name__ == '__main__':
    app = DiseasePredictorApp(DecisionTreeStrategy)
    start_server(app.run, port=8082, debug=True)# updated to refresh commit label
# updated to refresh commit label
