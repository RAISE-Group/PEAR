def test_doc_string(self):
    df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
    df
    df.ewm(com=0.5).mean()