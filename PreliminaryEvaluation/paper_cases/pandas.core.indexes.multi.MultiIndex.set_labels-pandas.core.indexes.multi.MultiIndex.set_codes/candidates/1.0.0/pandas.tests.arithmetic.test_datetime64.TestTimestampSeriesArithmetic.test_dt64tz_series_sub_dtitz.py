def test_dt64tz_series_sub_dtitz(self):
    dti = pd.date_range('1999-09-30', periods=10, tz='US/Pacific')
    ser = pd.Series(dti)
    expected = pd.Series(pd.TimedeltaIndex(['0days'] * 10))
    res = dti - ser
    tm.assert_series_equal(res, expected)
    res = ser - dti
    tm.assert_series_equal(res, expected)