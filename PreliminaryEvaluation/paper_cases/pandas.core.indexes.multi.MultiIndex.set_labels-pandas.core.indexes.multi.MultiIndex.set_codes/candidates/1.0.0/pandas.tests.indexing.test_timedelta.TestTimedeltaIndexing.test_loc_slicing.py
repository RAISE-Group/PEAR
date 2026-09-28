def test_loc_slicing(self):
    ix = pd.timedelta_range(start='1 day', end='2 days', freq='1H')
    ser = ix.to_series()
    result = ser.loc[:ix[-2]]
    expected = ser.iloc[:-1]
    tm.assert_series_equal(result, expected)