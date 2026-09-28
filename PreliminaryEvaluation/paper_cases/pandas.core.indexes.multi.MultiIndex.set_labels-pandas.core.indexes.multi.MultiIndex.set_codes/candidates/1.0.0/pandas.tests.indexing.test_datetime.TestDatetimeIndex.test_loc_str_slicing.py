def test_loc_str_slicing(self):
    ix = pd.period_range(start='2017-01-01', end='2018-01-01', freq='M')
    ser = ix.to_series()
    result = ser.loc[:'2017-12']
    expected = ser.iloc[:-1]
    tm.assert_series_equal(result, expected)