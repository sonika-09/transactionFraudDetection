# 🕵️‍♀️Transaction Fraud Detector

A machine learning project to detect fraudulent credit card transactions using a Random Forest classifier and Streamlit for a simple web interface.

## How it works
1. **Dataset**
- This model is trained on the Kaggle Credit Card Fraud Detection dataset.
- link - https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

2. **Preprocessing**
- Dropped the Class column during prediction
- Balanced dataset using SMOTE
- Trained a RandomForestClassifier

3. **Model Output**
- The model and expected input columns are saved using joblib

4. **Web Interface**
- Built with Streamlit
- Upload a CSV of transactions and get predictions for each entry

## How to use
1. Create a Virtual Environment
- `python -m venv venv`
- `.\venv\Scripts\Activate.ps1`
2. Install Requirements
- `pip install -r requiremnts.txt`
3. Run the App
- `streamlit run app.py`

*The app will return a column called Prediction with 0 (Non-Fraud) or 1 (Fraud).*

## Model Info
- Algorithm: Random Forest
- Handling class imbalance with SMOTE
- Evaluated with confusion matrix and classification report
