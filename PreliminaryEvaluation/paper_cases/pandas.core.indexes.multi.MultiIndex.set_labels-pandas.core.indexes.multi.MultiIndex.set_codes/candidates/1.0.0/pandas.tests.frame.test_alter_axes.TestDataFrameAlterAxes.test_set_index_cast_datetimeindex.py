def test_set_index_cast_datetimeindex(self):
    df = DataFrame({'A': [datetime(2000, 1, 1) + timedelta(i) for i in range(1000)], 'B': np.random.randn(1000)})
    idf = df.set_index('A')
    assert isinstance(idf.index, DatetimeIndex)