from src.data_manager import load_transactions
from src.budget import calculate_budget_summary


df = load_transactions("data/transactions.csv")


def test_budget_summary():

    budget_summary = calculate_budget_summary(df)

    shopping = None

    for item in budget_summary:
        if item["category"] == "Shopping":
            shopping = item

    assert shopping is not None
    assert shopping["budget"] == 7000
    assert shopping["actual_spending"] == 8750
    assert shopping["remaining"] == -1750