def test_doc_string(self):
    df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
    df
    df.rolling(2).sum()
    df.rolling(2, min_periods=1).sum()