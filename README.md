# 🛡️ FraudRadar — AI-Powered Transaction Fraud Detection

FraudRadar is a machine learning web application that analyzes financial transaction details and predicts whether a transaction may be fraudulent. Built with Python and Streamlit, it provides a simple, interactive interface for demonstrating transaction fraud classification.

## ✨ Features

- **Transaction Analysis:** Enter transaction type, amount, and sender/receiver balances.
- **Machine Learning:** Uses a trained Logistic Regression classification pipeline.
- **Feature Engineering:** Calculates sender and receiver balance differences.
- **Interactive Dashboard:** Clean Streamlit interface with visual prediction results.
- **Real-Time Inference:** Generates predictions from user-provided transaction details.

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## ⚙️ How It Works

1. Enter the transaction details.
2. The app calculates the derived balance-difference features.
3. The trained preprocessing and classification pipeline processes the input.
4. FraudRadar displays whether the model flags the transaction as potentially fraudulent.

## 🚀 Run Locally

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FraudRadar
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Start the application**

```bash
python -m streamlit run fraud_detection.py
```

## 📁 Project Structure

```text
FraudRadar/
├── fraud_detection.py
├── fraud_detection_pipeline.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚠️ Disclaimer

FraudRadar is an educational machine learning project. Its predictions are estimates and should not be used as the sole basis for real financial decisions. A transaction classified as legitimate may still be fraudulent.

## 👩‍💻 Author

Sakshi Joshi

Developed as a machine learning and financial fraud detection project.
**Project:** FraudRadar — AI-Powered Transaction Intelligence
