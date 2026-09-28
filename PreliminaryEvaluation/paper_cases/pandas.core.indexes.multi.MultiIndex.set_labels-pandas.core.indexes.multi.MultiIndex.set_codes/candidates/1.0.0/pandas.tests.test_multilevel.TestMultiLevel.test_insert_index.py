def test_insert_index(self):
    df = self.ymd[:5].T
    df[2000, 1, 10] = df[2000, 1, 7]
    assert isinstance(df.columns, MultiIndex)
    assert (df[2000, 1, 10] == df[2000, 1, 7]).all()