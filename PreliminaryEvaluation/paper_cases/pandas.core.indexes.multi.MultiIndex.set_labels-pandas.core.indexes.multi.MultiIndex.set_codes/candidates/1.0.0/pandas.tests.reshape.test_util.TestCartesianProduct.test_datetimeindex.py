def test_datetimeindex(self):
    x = date_range('2000-01-01', periods=2)
    result1, result2 = [Index(y).day for y in cartesian_product([x, x])]
    expected1 = Index([1, 1, 2, 2])
    expected2 = Index([1, 2, 1, 2])
    tm.assert_index_equal(result1, expected1)
    tm.assert_index_equal(result2, expected2)