def generate_savings_insight(savings_rate):
    if savings_rate >= 50:
        return f"Excellent savings rate of {savings_rate:.2f}%."
    elif savings_rate >= 30:
        return f"Good savings rate of {savings_rate:.2f}%."
    elif savings_rate >= 20:
        return f"Moderate savings rate of {savings_rate:.2f}%."
    else:
        return f"Low savings rate of {savings_rate:.2f}%."


def generate_spending_insight(category_spending):
    highest_category = category_spending.idxmax()
    highest_amount = category_spending.max()

    return (
        f"Highest spending category is "
        f"{highest_category} with ₹{highest_amount} spent."
    )


def generate_budget_insight(budget_summary):
    over_budget = [
        item for item in budget_summary
        if item["remaining"] < 0
    ]

    if not over_budget:
        return "All categories are within budget."

    insights = []

    for item in over_budget:
        overspent_amount = abs(item["remaining"])

        insights.append(
            f"{item['category']} is over budget by ₹{overspent_amount}."
        )

    return " ".join(insights)