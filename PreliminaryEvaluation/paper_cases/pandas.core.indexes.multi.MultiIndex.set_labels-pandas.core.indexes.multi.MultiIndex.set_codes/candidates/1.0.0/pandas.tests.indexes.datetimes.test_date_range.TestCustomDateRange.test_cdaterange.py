def test_cdaterange(self):
    result = bdate_range('2013-05-01', periods=3, freq='C')
    expected = DatetimeIndex(['2013-05-01', '2013-05-02', '2013-05-03'])
    tm.assert_index_equal(result, expected)