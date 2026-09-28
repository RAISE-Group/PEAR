def test_objarr_radd_str(self, box):
    ser = pd.Series(['x', np.nan, 'x'])
    expected = pd.Series(['ax', np.nan, 'ax'])
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    result = 'a' + ser
    tm.assert_equal(result, expected)