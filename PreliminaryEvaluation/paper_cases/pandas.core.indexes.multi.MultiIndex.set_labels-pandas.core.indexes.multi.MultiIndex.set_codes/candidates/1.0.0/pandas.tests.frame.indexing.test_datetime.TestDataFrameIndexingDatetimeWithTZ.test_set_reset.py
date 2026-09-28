def test_set_reset(self):
    idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
    df = DataFrame({'A': [0, 1, 2]}, index=idx)
    result = df.reset_index()
    assert result['foo'].dtype, 'M8[ns, US/Eastern'
    df = result.set_index('foo')
    tm.assert_index_equal(df.index, idx)