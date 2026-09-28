def test_shift_fill_value(self):
    ts = Series([1.0, 2.0, 3.0, 4.0, 5.0], index=date_range('1/1/2000', periods=5, freq='H'))
    exp = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=date_range('1/1/2000', periods=5, freq='H'))
    result = ts.shift(1, fill_value=0.0)
    tm.assert_series_equal(result, exp)
    exp = Series([0.0, 0.0, 1.0, 2.0, 3.0], index=date_range('1/1/2000', periods=5, freq='H'))
    result = ts.shift(2, fill_value=0.0)
    tm.assert_series_equal(result, exp)
    ts = pd.Series([1, 2, 3])
    res = ts.shift(2, fill_value=0)
    assert res.dtype == ts.dtype