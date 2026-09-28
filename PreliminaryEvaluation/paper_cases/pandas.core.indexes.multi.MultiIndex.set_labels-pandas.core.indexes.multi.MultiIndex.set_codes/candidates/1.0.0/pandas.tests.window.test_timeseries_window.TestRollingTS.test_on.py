def test_on(self):
    df = self.regular
    with pytest.raises(ValueError):
        df.rolling(window='2s', on='foobar')
    df = df.copy()
    df['C'] = date_range('20130101', periods=len(df))
    df.rolling(window='2d', on='C').sum()
    with pytest.raises(ValueError):
        df.rolling(window='2d', on='B')
    df.rolling(window='2d', on='C').B.sum()