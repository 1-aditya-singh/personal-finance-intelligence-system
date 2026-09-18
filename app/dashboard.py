import streamlit as st
import pandas as pd
from src.data_manager import load_transactions
from src.insights import (
    generate_savings_insight,
    generate_spending_insight,
    generate_budget_insight
)



from src.analytics import (
    calculate_total_income,
    calculate_total_expense,
    calculate_savings,
    calculate_savings_rate
)


st.set_page_config(
    page_title="Personal Finance Intelligence",
    page_icon="💰",
    layout="wide"
)


st.title("💰 Personal Finance Intelligence System")

st.write(
    "An interactive dashboard for analyzing personal income, "
    "expenses, savings, budgets, and spending behavior."
)


df = load_transactions("data/transactions.csv")


total_income = calculate_total_income(df)
total_expense = calculate_total_expense(df)
savings = calculate_savings(df)
savings_rate = calculate_savings_rate(df)



col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Income",
    f"₹{total_income:,.0f}"
)


col2.metric(
    "Total Expense",
    f"₹{total_expense:,.0f}"
)


col3.metric(
    "Savings",
    f"₹{savings:,.0f}"
)


col4.metric(
    "Savings Rate",
    f"{savings_rate:.2f}%"
)



st.divider()

st.header("📊 Spending by Category")

expenses = df[df["type"] == "Expense"]

category_spending = (
    expenses
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_spending)

st.divider()

st.header("📈 Monthly Financial Performance")

df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_income = (
    df[df["type"] == "Income"]
    .groupby("month")["amount"]
    .sum()
)

monthly_expense = (
    df[df["type"] == "Expense"]
    .groupby("month")["amount"]
    .sum()
)

monthly_summary = (
    monthly_income
    .to_frame("Income")
    .join(monthly_expense.to_frame("Expense"))
)

monthly_summary["Savings"] = (
    monthly_summary["Income"] -
    monthly_summary["Expense"]
)

st.line_chart(monthly_summary)


st.divider()

st.header("🎯 Budget Tracking")

from src.budget import calculate_budget_summary

budget_summary = calculate_budget_summary(df)

budget_df = pd.DataFrame(budget_summary)

st.dataframe(
    budget_df,
    use_container_width=True
)

st.divider()

st.header("💡 Financial Insights")

st.info(
    generate_savings_insight(savings_rate)
)

st.info(
    generate_spending_insight(category_spending)
)

st.warning(
    generate_budget_insight(budget_summary)
)

st.divider()

st.header("🚨 Spending Alerts")

average_expense = expenses["amount"].mean()

high_expense_limit = average_expense * 2

high_expenses = expenses[
    expenses["amount"] > high_expense_limit
]

if len(high_expenses) > 0:

    st.warning(
        f"{len(high_expenses)} expenses are significantly "
        f"higher than the average expense."
    )

    st.dataframe(
        high_expenses[
            ["date", "category", "amount", "description"]
        ],
        use_container_width=True
    )

else:

    st.success("No unusually high expenses detected.")


st.divider()

st.header("🔎 Expense Anomaly Detection")

std_expense = expenses["amount"].std()

anomaly_threshold = (
    average_expense +
    (2 * std_expense)
)

anomalies = expenses[
    expenses["amount"] > anomaly_threshold
]

st.write(
    f"Anomaly threshold: ₹{anomaly_threshold:,.2f}"
)

if len(anomalies) > 0:

    st.error(
        f"{len(anomalies)} unusual expenses detected."
    )

    st.dataframe(
        anomalies[
            ["date", "category", "amount", "description"]
        ],
        use_container_width=True
    )

else:

    st.success("No unusual expenses detected.")


st.divider()

st.caption(
    "Personal Finance Intelligence System | "
    "Built with Python, Pandas, Matplotlib, Seaborn and Streamlit"
)