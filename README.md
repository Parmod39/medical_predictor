# 🩺 Medical Predictor

This project is a machine learning–powered medical prediction system that allows users to input relevant health data and receive predictive outcomes using customizable strategies. The app includes a user-friendly interface, data preprocessing pipeline, and pluggable machine learning logic.

## 🌐 Live Demo

🔗 Visit the live app: [https://parmod02.pythonanywhere.com/](https://parmod02.pythonanywhere.com/)

## 🧠 Features

- 📊 **User Interface** built with PyWebIO for seamless interaction.
- 🧹 **Data Preprocessing** using `data_loader.py` to clean and structure inputs.
- 🌲 **Decision Tree Strategy** and abstract base to plug in future ML models.
- 🧩 **Modular Design** using the Strategy pattern for flexibility and extensibility.

## 📁 Project Structure

medical_predictor/
│
├── main.py # App entry point
├── app.py # UI logic for user input and prediction flow
├── data_loader.py # Prepares and cleans input data
├── decision_tree_strategy.py# Implements prediction using Decision Tree
├── predictor_strategy.py # Base strategy class for extensible ML logic
└── init.py # Marks directory as a Python package


## 🚀 Getting Started (Local Run)

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Parmod39/medical_predictor.git
   cd medical_predictor

2.Install requirements (create requirements.txt if not already):
  ```bash
  pip install pywebio scikit-learn pandas

3.Run the app:
  ```bash
  python main.py

##📬 Author
Parmod Budhiraja
GitHub: Parmod39
Live App: https://parmod02.pythonanywhere.com/