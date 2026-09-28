def test_objarr_add_str(self, box):
    ser = pd.Series(['x', np.nan, 'x'])
    expected = pd.Series(['xa', np.nan, 'xa'])
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    result = ser + 'a'
    tm.assert_equal(result, expected)