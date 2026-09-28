def test_dti_set_index_reindex(self):
    df = DataFrame(np.random.random(6))
    idx1 = date_range('2011/01/01', periods=6, freq='M', tz='US/Eastern')
    idx2 = date_range('2013', periods=6, freq='A', tz='Asia/Tokyo')
    df = df.set_index(idx1)
    tm.assert_index_equal(df.index, idx1)
    df = df.reindex(idx2)
    tm.assert_index_equal(df.index, idx2)
    index = date_range(datetime(2015, 10, 1), datetime(2015, 10, 1, 23), freq='H', tz='US/Eastern')
    df = DataFrame(np.random.randn(24, 1), columns=['a'], index=index)
    new_index = date_range(datetime(2015, 10, 2), datetime(2015, 10, 2, 23), freq='H', tz='US/Eastern')
    result = df.set_index(new_index)
    assert result.index.freq == index.freq