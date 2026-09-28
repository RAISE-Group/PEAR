def test_loc_label_slicing(self):
    ix = pd.period_range(start='2017-01-01', end='2018-01-01', freq='M')
    ser = ix.to_series()
    result = ser.loc[:ix[-2]]
    expected = ser.iloc[:-1]
    tm.assert_series_equal(result, expected)