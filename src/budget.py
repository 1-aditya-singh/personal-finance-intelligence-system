def get_budgets():
    return {
        "Food": 5000,
        "Shopping": 7000,
        "Travel": 5000,
        "Bills": 4000,
        "Education": 3000,
        "Entertainment": 3000,
        "Health": 2500
    }


def calculate_budget_summary(df):
    expenses = df[df["type"] == "Expense"]

    category_spending = (
        expenses
        .groupby("category")["amount"]
        .sum()
    )

    budgets = get_budgets()

    budget_data = []

    for category, budget in budgets.items():

        actual = category_spending.get(category, 0)

        remaining = budget - actual

        budget_data.append({
            "category": category,
            "budget": budget,
            "actual_spending": actual,
            "remaining": remaining
        })

    return budget_data