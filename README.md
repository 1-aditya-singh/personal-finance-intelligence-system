# 💰 Personal Finance Intelligence System

A Python-based personal finance analysis and intelligence system that analyzes income, expenses, savings, budgets, spending behavior, financial health, and unusual expenses.

The project started as a data analysis workflow using Pandas and gradually evolved into a modular Python application with automated testing and an interactive Streamlit dashboard.

---

## 📌 Project Overview

Managing personal finances can be difficult when financial transactions are stored as raw data.

This project transforms transaction data into meaningful financial information such as:

- Total income
- Total expenses
- Savings
- Savings rate
- Category-wise spending
- Monthly financial performance
- Budget utilization
- Financial health score
- Spending alerts
- Financial insights
- Expense anomaly detection

The project also provides an interactive dashboard for exploring financial information.

---

## 🎯 Problem Statement

Raw financial transaction data does not directly provide useful information about spending patterns or financial performance.

The goal of this project is to build a system that can:

1. Analyze financial transactions.
2. Identify spending patterns.
3. Track budgets.
4. Calculate savings and savings rate.
5. Generate financial insights.
6. Detect unusually large expenses.
7. Present the results through an interactive dashboard.

---

## 🚀 Features

### Financial Analysis

- Total income calculation
- Total expense calculation
- Savings calculation
- Savings rate calculation
- Average expense analysis
- Largest expense detection

### Spending Analysis

- Category-wise spending
- Daily expense analysis
- Monthly expense analysis
- Spending behavior analysis
- Top expense identification

### Financial Intelligence

- Financial health score
- Spending alerts
- Budget tracking
- Savings analysis
- Automated financial insights
- Expense anomaly detection

### Visualization

- Income vs Expense
- Spending by category
- Monthly savings
- Monthly savings rate
- Monthly financial performance
- Expense distribution
- Category-month spending heatmap

### Application

- Interactive Streamlit dashboard
- Automated tests using pytest
- Modular Python architecture

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
- Git & GitHub

---

## 📂 Project Structure

```text
personal-finance-intelligence/
│
├── app/
│   └── dashboard.py
│
├── data/
│   └── transactions.csv
│
├── notebooks/
│   ├── financial_analysis.ipynb
│   ├── monthly_analysis.ipynb
│   ├── daily_analysis.ipynb
│   ├── spending_behavior.ipynb
│   ├── top_expenses.ipynb
│   ├── financial_functions.ipynb
│   ├── financial_health.ipynb
│   ├── spending_alerts.ipynb
│   ├── budget_tracking.ipynb
│   ├── savings_analysis.ipynb
│   ├── financial_insights.ipynb
│   ├── financial_visualizations.ipynb
│   ├── advanced_visual_analysis.ipynb
│   └── expense_anomaly_detection.ipynb
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
├── screenshots/
│   ├── dashboard_overview.jpeg
│   ├── dashboard_analysis.jpeg
│   └── dashboard_alerts.jpeg
│
├── .gitignore
├── README.md
└── requirements.txt