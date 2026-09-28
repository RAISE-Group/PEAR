def test_map(self):
    rng = timedelta_range('1 day', periods=10)
    f = lambda x: x.days
    result = rng.map(f)
    exp = Int64Index([f(x) for x in rng])
    tm.assert_index_equal(result, exp)