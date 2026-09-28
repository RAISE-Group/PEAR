def test_numeric_columns(self):
    df = pd.DataFrame({0: [1, 2, 3]})
    df.style._translate()