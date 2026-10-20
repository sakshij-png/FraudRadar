# 🛡️ FraudRadar — AI-Powered Transaction Fraud Detection

FraudRadar is a machine learning web application that analyzes financial transaction details and predicts whether a transaction may be fraudulent. Built with **Python and Streamlit**, it provides a simple, interactive interface for demonstrating transaction fraud classification.

## ✨ Features

- **Transaction Analysis:** Enter transaction type, amount, and sender/receiver balances.
- **Machine Learning:** Uses a trained Logistic Regression classification pipeline.
- **Feature Engineering:** Calculates sender and receiver balance differences.
- **Interactive Dashboard:** Clean Streamlit interface with visual prediction results.
- **Real-Time Inference:** Generates predictions from user-provided transaction details.
- **Web-Based Interface:** Access the application through a browser without manually running prediction code.

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## ⚙️ How It Works

1. **Input:** The user enters transaction details, including transaction type, amount, and account balances.
2. **Feature Engineering:** The application calculates balance differences for the sender and receiver.
3. **Preprocessing:** The trained pipeline processes numerical and categorical features.
4. **Prediction:** The classification model evaluates the transaction.
5. **Result:** The application displays whether the transaction is predicted to be potentially fraudulent or legitimate.

### Features Used

- Transaction type
- Transaction amount
- Original sender balance
- New sender balance
- Original receiver balance
- New receiver balance
- Sender balance difference
- Receiver balance difference

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone (https://github.com/sakshij-png/FraudRadar.git)
cd FraudRadar
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the application

```bash
python -m streamlit run fraud_detection.py
```

Open the local URL displayed in your terminal to use FraudRadar.

## 📁 Project Structure

```text
FraudRadar/
├── fraud_detection.py
├── fraud_detection_pipeline.pkl
├── analysis_model.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Project Objective

This project demonstrates the application of machine learning to a financial fraud detection use case. It combines model development, feature engineering, preprocessing, prediction, and web application deployment into a single workflow.

## 🔮 Future Enhancements

- Add transaction risk scores and confidence indicators.
- Develop a dashboard for transaction monitoring and analytics.
- Evaluate additional classification algorithms.
- Add model evaluation metrics and explainability tools.
- Improve input validation and user guidance.
- Explore batch prediction for multiple transactions.

## ⚠️ Disclaimer

FraudRadar is an educational machine learning project. Its predictions are estimates and should not be used as the sole basis for real financial decisions. A transaction classified as legitimate may still be fraudulent.

## 👩‍💻 Author

**Sakshi Joshi**

*Project: FraudRadar — AI-Powered Transaction Intelligence*

Developed as a machine learning and financial fraud detection project.

