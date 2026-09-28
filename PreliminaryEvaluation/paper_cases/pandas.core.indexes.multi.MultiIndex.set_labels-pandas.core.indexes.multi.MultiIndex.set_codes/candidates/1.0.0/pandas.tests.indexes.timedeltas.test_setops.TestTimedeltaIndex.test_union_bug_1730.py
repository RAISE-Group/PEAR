def test_union_bug_1730(self):
    rng_a = timedelta_range('1 day', periods=4, freq='3H')
    rng_b = timedelta_range('1 day', periods=4, freq='4H')
    result = rng_a.union(rng_b)
    exp = TimedeltaIndex(sorted(set(rng_a) | set(rng_b)))
    tm.assert_index_equal(result, exp)