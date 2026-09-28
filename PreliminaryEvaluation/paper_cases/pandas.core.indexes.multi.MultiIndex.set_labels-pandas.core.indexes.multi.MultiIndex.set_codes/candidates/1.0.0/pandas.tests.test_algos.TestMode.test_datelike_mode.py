def test_datelike_mode(self):
    exp = Series(['1900-05-03', '2011-01-03', '2013-01-02'], dtype='M8[ns]')
    s = Series(['2011-01-03', '2013-01-02', '1900-05-03'], dtype='M8[ns]')
    tm.assert_series_equal(algos.mode(s), exp)
    exp = Series(['2011-01-03', '2013-01-02'], dtype='M8[ns]')
    s = Series(['2011-01-03', '2013-01-02', '1900-05-03', '2011-01-03', '2013-01-02'], dtype='M8[ns]')
    tm.assert_series_equal(algos.mode(s), exp)