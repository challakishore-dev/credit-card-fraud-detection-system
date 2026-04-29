# 💳 Credit Card Fraud Detection System

A production-style Machine Learning project built to detect fraudulent credit card transactions using transaction behavior patterns, anomaly indicators, and predictive analytics.

This project simulates how banks, fintech companies, and payment gateways use Machine Learning to identify suspicious transactions in real time, reduce fraud losses, and improve customer trust.

---

## 🚀 Overview

Credit card fraud is one of the most common financial crimes in digital payments. Millions of transactions happen daily, making manual fraud detection impossible.

This project uses Machine Learning to classify transactions as:

* ✅ Legitimate
* 🚨 Fraudulent
* ⚠️ Needs Manual Review

It demonstrates a complete end-to-end workflow including data generation, preprocessing, model training, API deployment, and dashboard visualization.

---

## 🎯 Objectives

* Detect fraudulent transactions accurately
* Reduce false positives and false negatives
* Build a real-time scoring API
* Create an interactive fraud dashboard
* Showcase practical Data Science and ML skills

---

## ✨ Features

* Machine Learning fraud prediction model
* Imbalanced dataset handling using SMOTE
* Random Forest Classifier
* FastAPI backend for prediction API
* Interactive UI dashboard
* Real-time fraud probability scoring
* Automated dataset generation
* Automated training pipeline
* Confusion matrix visualization

---

## 🛠 Tech Stack

### Languages & Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Tools

* Joblib
* Git
* GitHub

---

## 📂 Project Structure

```
credit-card-fraud-detection-system/
│── data/
│── models/
│── outputs/
│── src/
│── templates/
│── app.py
│── start.py
│── run_project.bat
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone Repository

```bash 
git clone https://github.com/challakishore-dev/credit-card-fraud-detection-system.git
cd credit-card-fraud-detection-system
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Start Project

```
python start.py
```

### Windows Users

Double-click:

```
run_project.bat
```

### Open Browser

```
http://127.0.0.1:8000
```

---

## 📊 Input Fields

| Field                | Description                   |
| -------------------- | ----------------------------- |
| Amount               | Transaction amount            |
| Hour                 | Time of transaction (0–23)    |
| Transactions Last 1h | Number of recent transactions |
| International        | 0 = No, 1 = Yes               |
| Night                | 0 = Day, 1 = Night            |

---

## 📈 Example Prediction

### Input

```
Amount: 3000
Hour: 2
Transactions Last 1h: 8
International: 1
Night: 1
```

### Output

```
Fraud Probability: 94.60%
Decision: REVIEW
```

---

## 🧠 Machine Learning Workflow

```
Transaction Data
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
SMOTE Balancing
      ↓
Model Training
      ↓
Prediction API
      ↓
Fraud Dashboard
```

---

## 📌 Why This Project Matters

Fraud detection systems are used across:

* Banking
* Fintech
* Credit Cards
* E-commerce Payments
* Wallet Apps
* Insurance Risk Systems
* BNPL Platforms

This project reflects real-world business use cases where fast and accurate decisions are critical.

---

## 📷 Screenshots

### Dashboard UI

<img width="1920" height="1080" alt="Screenshot (162)" src="https://github.com/user-attachments/assets/89849b17-c9e6-4941-9f8e-27c70941a407" />

<img width="1920" height="1080" alt="Screenshot (163)" src="https://github.com/user-attachments/assets/283b5e04-b893-4806-a4dc-106b63d6e1cc" />

<img width="1920" height="1080" alt="Screenshot (164)" src="https://github.com/user-attachments/assets/48a444b5-8aaf-469c-a5e3-789966a99acb" />

<img width="1920" height="1080" alt="Screenshot (165)" src="https://github.com/user-attachments/assets/96776da0-1a6b-4509-a823-6f60ed42237a" />

### Confusion Matrix

<img width="568" height="451" alt="confusion_matrix" src="https://github.com/user-attachments/assets/8e8c23fc-4ede-4cfe-90b0-07c41901e853" />


## 💼 Resume Description

Built an end-to-end Credit Card Fraud Detection System using Random Forest, SMOTE, FastAPI, and an interactive dashboard for real-time fraud risk scoring.

---

## 🔥 Future Enhancements

* XGBoost / LightGBM models
* SHAP Explainable AI
* Live analytics dashboard
* CSV bulk upload scoring
* Docker deployment
* Cloud hosting
* CI/CD pipeline

---

## 👨‍💻 Author

# Challa Kishore 

# GitHub: https://github.com/challakishore-dev

# LinkedIn: https://linkedin.com/in/challa-kishore-a817552b4


## ⭐ Support

If you found this project useful, please give it a star.
