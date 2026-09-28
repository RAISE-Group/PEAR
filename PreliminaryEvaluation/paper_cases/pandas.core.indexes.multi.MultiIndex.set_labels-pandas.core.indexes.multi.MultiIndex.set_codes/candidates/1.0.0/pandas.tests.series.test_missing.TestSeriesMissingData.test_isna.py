def test_isna(self):
    ser = Series([0, 5.4, 3, np.nan, -0.001])
    expected = Series([False, False, False, True, False])
    tm.assert_series_equal(ser.isna(), expected)
    ser = Series(['hi', '', np.nan])
    expected = Series([False, False, True])
    tm.assert_series_equal(ser.isna(), expected)