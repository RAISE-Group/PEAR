def test_from_dict(self):
    idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
    dr = date_range('20130110', periods=3)
    df = DataFrame({'A': idx, 'B': dr})
    assert df['A'].dtype, 'M8[ns, US/Eastern'
    assert df['A'].name == 'A'
    tm.assert_series_equal(df['A'], Series(idx, name='A'))
    tm.assert_series_equal(df['B'], Series(dr, name='B'))