def test_nlargest_duplicate_keep_all_ties(self):
    ser = Series([10, 9, 8, 7, 7, 7, 7, 6])
    result = ser.nlargest(4, keep='all')
    expected = Series([10, 9, 8, 7, 7, 7, 7])
    tm.assert_series_equal(result, expected)
    result = ser.nsmallest(2, keep='all')
    expected = Series([6, 7, 7, 7, 7], index=[7, 3, 4, 5, 6])
    tm.assert_series_equal(result, expected)