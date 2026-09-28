def test_union_bug_4564(self):
    left = timedelta_range('1 day', '30d')
    right = left + pd.offsets.Minute(15)
    result = left.union(right)
    exp = TimedeltaIndex(sorted(set(left) | set(right)))
    tm.assert_index_equal(result, exp)