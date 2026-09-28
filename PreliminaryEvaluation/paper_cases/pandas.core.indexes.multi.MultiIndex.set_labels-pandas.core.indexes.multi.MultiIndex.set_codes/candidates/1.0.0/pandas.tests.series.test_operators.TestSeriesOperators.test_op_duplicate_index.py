def test_op_duplicate_index(self):
    s1 = Series([1, 2], index=[1, 1])
    s2 = Series([10, 10], index=[1, 2])
    result = s1 + s2
    expected = pd.Series([11, 12, np.nan], index=[1, 1, 2])
    tm.assert_series_equal(result, expected)