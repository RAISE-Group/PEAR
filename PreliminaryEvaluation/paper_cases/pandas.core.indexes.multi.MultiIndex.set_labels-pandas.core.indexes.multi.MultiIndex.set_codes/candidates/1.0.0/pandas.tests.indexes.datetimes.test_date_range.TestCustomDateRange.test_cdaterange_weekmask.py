def test_cdaterange_weekmask(self):
    result = bdate_range('2013-05-01', periods=3, freq='C', weekmask='Sun Mon Tue Wed Thu')
    expected = DatetimeIndex(['2013-05-01', '2013-05-02', '2013-05-05'])
    tm.assert_index_equal(result, expected)
    msg = 'a custom frequency string is required when holidays or weekmask are passed, got frequency B'
    with pytest.raises(ValueError, match=msg):
        bdate_range('2013-05-01', periods=3, weekmask='Sun Mon Tue Wed Thu')