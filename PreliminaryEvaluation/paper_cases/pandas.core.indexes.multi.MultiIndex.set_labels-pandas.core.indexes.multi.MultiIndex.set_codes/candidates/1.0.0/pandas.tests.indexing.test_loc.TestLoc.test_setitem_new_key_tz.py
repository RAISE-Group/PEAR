def test_setitem_new_key_tz(self):
    vals = [pd.to_datetime(42).tz_localize('UTC'), pd.to_datetime(666).tz_localize('UTC')]
    expected = pd.Series(vals, index=['foo', 'bar'])
    ser = pd.Series(dtype=object)
    ser['foo'] = vals[0]
    ser['bar'] = vals[1]
    tm.assert_series_equal(ser, expected)
    ser = pd.Series(dtype=object)
    ser.loc['foo'] = vals[0]
    ser.loc['bar'] = vals[1]
    tm.assert_series_equal(ser, expected)