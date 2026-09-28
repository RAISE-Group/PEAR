def test_mixed_datetime64(self):
    df = DataFrame({'A': [1, 2], 'B': ['2012-01-01', '2012-01-02']})
    df['B'] = pd.to_datetime(df.B)
    result = repr(df.loc[0])
    assert '2012-01-01' in result