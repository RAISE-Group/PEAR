def test_dataframe_repr(self, data):
    df = pd.DataFrame({'A': data})
    repr(df)