def test_offset_whole_year(self):
    dates = (datetime(2007, 12, 31), datetime(2008, 1, 15), datetime(2008, 1, 31), datetime(2008, 2, 15), datetime(2008, 2, 29), datetime(2008, 3, 15), datetime(2008, 3, 31), datetime(2008, 4, 15), datetime(2008, 4, 30), datetime(2008, 5, 15), datetime(2008, 5, 31), datetime(2008, 6, 15), datetime(2008, 6, 30), datetime(2008, 7, 15), datetime(2008, 7, 31), datetime(2008, 8, 15), datetime(2008, 8, 31), datetime(2008, 9, 15), datetime(2008, 9, 30), datetime(2008, 10, 15), datetime(2008, 10, 31), datetime(2008, 11, 15), datetime(2008, 11, 30), datetime(2008, 12, 15), datetime(2008, 12, 31))
    for base, exp_date in zip(dates[:-1], dates[1:]):
        assert_offset_equal(SemiMonthEnd(), base, exp_date)
    s = DatetimeIndex(dates[:-1])
    with tm.assert_produces_warning(None):
        result = SemiMonthEnd().apply_index(s)
    exp = DatetimeIndex(dates[1:])
    tm.assert_index_equal(result, exp)
    result = date_range(start=dates[0], end=dates[-1], freq='SM')
    exp = DatetimeIndex(dates)
    tm.assert_index_equal(result, exp)