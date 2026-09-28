def test_notna(self):
    ser = Series([0, 5.4, 3, np.nan, -0.001])
    expected = Series([True, True, True, False, True])
    tm.assert_series_equal(ser.notna(), expected)
    ser = Series(['hi', '', np.nan])
    expected = Series([True, True, False])
    tm.assert_series_equal(ser.notna(), expected)