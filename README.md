# 💰 Personal Finance Intelligence System

A Python-based personal finance analysis and intelligence system that transforms raw transaction data into meaningful financial insights.

The project analyzes income, expenses, savings, budgets, spending behavior, financial health, alerts, and unusual expenses through a modular Python application and an interactive Streamlit dashboard.

---

## 📌 Project Overview

Managing personal finances becomes difficult when transaction data is stored as raw records without meaningful analysis.

This project converts transaction data into useful financial information such as:

- Total income
- Total expenses
- Savings
- Savings rate
- Category-wise spending
- Monthly financial performance
- Daily spending behavior
- Budget utilization
- Financial health score
- Spending alerts
- Financial insights
- Expense anomaly detection

The project started as a collection of data analysis notebooks and gradually evolved into a modular Python application with automated testing and an interactive Streamlit dashboard.

---

## 🎯 Problem Statement

Raw financial transaction data does not directly explain spending patterns or overall financial performance.

The goal of this project is to build a system that can:

1. Analyze financial transactions.
2. Calculate income, expenses, savings, and savings rate.
3. Identify spending patterns.
4. Analyze daily and monthly spending.
5. Track category-wise budgets.
6. Generate financial health indicators.
7. Detect unusual expenses.
8. Generate actionable financial insights.
9. Present financial information through an interactive dashboard.

---

## 🚀 Features

### 💵 Financial Analysis

- Total income calculation
- Total expense calculation
- Savings calculation
- Savings rate calculation
- Average expense analysis
- Largest expense detection

### 📊 Spending Analysis

- Category-wise spending
- Daily expense analysis
- Monthly expense analysis
- Spending behavior analysis
- Top expense identification

### 🧠 Financial Intelligence

- Financial health score
- Spending alerts
- Budget tracking
- Savings analysis
- Automated financial insights
- Expense anomaly detection

### 📈 Data Visualization

- Income vs Expense
- Spending by category
- Monthly savings
- Monthly savings rate
- Monthly financial performance
- Expense distribution
- Category-month spending heatmap

### 🖥️ Application

- Interactive Streamlit dashboard
- Modular Python architecture
- Automated unit testing with pytest
- Reusable analysis functions

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Pytest
- Jupyter Notebook
- Git
- GitHub

---

## 📂 Project Structure

```text
personal-finance-intelligence-system/
│
├── app/
│   └── dashboard.py
│
├── data/
│   └── transactions.csv
│
├── notebooks/
│   ├── finance_analysis.ipynb
│   ├── financial_functions.ipynb
│   ├── daily_analysis.ipynb
│   ├── monthly_analysis.ipynb
│   ├── spending_behavior.ipynb
│   ├── top_expenses.ipynb
│   ├── financial_health.ipynb
│   ├── spending_alerts.ipynb
│   ├── budget_tracking.ipynb
│   ├── savings_analysis.ipynb
│   ├── financial_insights.ipynb
│   ├── financial_visualizations.ipynb
│   ├── advanced_visual_analysis.ipynb
│   └── expense_anomaly_detection.ipynb
│
├── screenshots/
│   ├── dashboard_overview.jpeg
│   ├── dashboard_analysis.jpeg
│   └── dashboard_alerts.jpeg
│
├── src/
│   ├── __init__.py
│   ├── analytics.py
│   ├── budget.py
│   ├── data_manager.py
│   ├── insights.py
│   └── utils.py
│
├── tests/
│   ├── test_analytics.py
│   ├── test_budget.py
│   └── test_transaction.py
│
├── .gitignore
├── README.md
└── requirements.txt