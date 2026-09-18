from src.data_manager import load_transactions


def test_load_transactions():

    df = load_transactions("data/transactions.csv")

    assert len(df) == 60
    assert "date" in df.columns
    assert "type" in df.columns
    assert "category" in df.columns
    assert "amount" in df.columns