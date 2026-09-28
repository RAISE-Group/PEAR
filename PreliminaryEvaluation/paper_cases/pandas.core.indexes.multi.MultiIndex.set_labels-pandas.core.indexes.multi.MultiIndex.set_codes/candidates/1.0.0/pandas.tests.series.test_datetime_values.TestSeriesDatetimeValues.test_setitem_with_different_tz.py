def test_setitem_with_different_tz(self):
    ser = pd.Series(pd.date_range('2000', periods=2, tz='US/Central'))
    ser[0] = pd.Timestamp('2000', tz='US/Eastern')
    expected = pd.Series([pd.Timestamp('2000-01-01 00:00:00-05:00', tz='US/Eastern'), pd.Timestamp('2000-01-02 00:00:00-06:00', tz='US/Central')], dtype=object)
    tm.assert_series_equal(ser, expected)