def test_dt64_series_arith_overflow(self):
    dt = pd.Timestamp('1700-01-31')
    td = pd.Timedelta('20000 Days')
    dti = pd.date_range('1949-09-30', freq='100Y', periods=4)
    ser = pd.Series(dti)
    msg = 'Overflow in int64 addition'
    with pytest.raises(OverflowError, match=msg):
        ser - dt
    with pytest.raises(OverflowError, match=msg):
        dt - ser
    with pytest.raises(OverflowError, match=msg):
        ser + td
    with pytest.raises(OverflowError, match=msg):
        td + ser
    ser.iloc[-1] = pd.NaT
    expected = pd.Series(['2004-10-03', '2104-10-04', '2204-10-04', 'NaT'], dtype='datetime64[ns]')
    res = ser + td
    tm.assert_series_equal(res, expected)
    res = td + ser
    tm.assert_series_equal(res, expected)
    ser.iloc[1:] = pd.NaT
    expected = pd.Series(['91279 Days', 'NaT', 'NaT', 'NaT'], dtype='timedelta64[ns]')
    res = ser - dt
    tm.assert_series_equal(res, expected)
    res = dt - ser
    tm.assert_series_equal(res, -expected)