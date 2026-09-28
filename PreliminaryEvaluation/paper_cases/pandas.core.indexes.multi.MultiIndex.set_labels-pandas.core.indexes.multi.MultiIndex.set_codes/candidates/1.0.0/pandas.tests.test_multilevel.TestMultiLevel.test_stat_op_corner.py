def test_stat_op_corner(self):
    obj = Series([10.0], index=MultiIndex.from_tuples([(2, 3)]))
    result = obj.sum(level=0)
    expected = Series([10.0], index=[2])
    tm.assert_series_equal(result, expected)