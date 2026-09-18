def calculate_total_income(df):
    income = df[df["type"] == "Income"]

    return income["amount"].sum()


def calculate_total_expense(df):
    expenses = df[df["type"] == "Expense"]

    return expenses["amount"].sum()


def calculate_savings(df):
    total_income = calculate_total_income(df)
    total_expense = calculate_total_expense(df)

    return total_income - total_expense


def calculate_savings_rate(df):
    total_income = calculate_total_income(df)
    savings = calculate_savings(df)

    return (savings / total_income) * 100


def calculate_average_expense(df):
    expenses = df[df["type"] == "Expense"]

    return expenses["amount"].mean()


def calculate_largest_expense(df):
    expenses = df[df["type"] == "Expense"]

    return expenses["amount"].max()