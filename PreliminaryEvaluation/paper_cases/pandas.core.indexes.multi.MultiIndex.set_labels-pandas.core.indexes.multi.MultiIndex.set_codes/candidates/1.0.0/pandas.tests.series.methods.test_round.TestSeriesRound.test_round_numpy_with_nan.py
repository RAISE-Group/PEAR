def test_round_numpy_with_nan(self):
    ser = Series([1.53, np.nan, 0.06])
    with tm.assert_produces_warning(None):
        result = ser.round()
    expected = Series([2.0, np.nan, 0.0])
    tm.assert_series_equal(result, expected)