from src.data_manager import load_transactions
from src.analytics import (
    calculate_total_income,
    calculate_total_expense,
    calculate_savings,
    calculate_savings_rate
)


df = load_transactions("data/transactions.csv")


def test_total_income():
    assert calculate_total_income(df) == 103000


def test_total_expense():
    assert calculate_total_expense(df) == 28200


def test_savings():
    assert calculate_savings(df) == 74800


def test_savings_rate():
    assert round(calculate_savings_rate(df), 2) == 72.62