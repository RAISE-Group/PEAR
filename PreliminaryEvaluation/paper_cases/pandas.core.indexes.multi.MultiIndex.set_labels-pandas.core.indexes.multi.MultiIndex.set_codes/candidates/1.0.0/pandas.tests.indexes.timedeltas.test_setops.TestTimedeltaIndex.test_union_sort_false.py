def test_union_sort_false(self):
    tdi = timedelta_range('1day', periods=5)
    left = tdi[3:]
    right = tdi[:3]
    assert left._can_fast_union(right)
    result = left.union(right)
    tm.assert_index_equal(result, tdi)
    result = left.union(right, sort=False)
    expected = pd.TimedeltaIndex(['4 Days', '5 Days', '1 Days', '2 Day', '3 Days'])
    tm.assert_index_equal(result, expected)