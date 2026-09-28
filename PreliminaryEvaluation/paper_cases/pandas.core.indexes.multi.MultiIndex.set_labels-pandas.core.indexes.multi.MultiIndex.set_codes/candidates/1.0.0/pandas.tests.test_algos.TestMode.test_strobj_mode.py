def test_strobj_mode(self):
    exp = ['b']
    data = ['a'] * 2 + ['b'] * 3
    s = Series(data, dtype='c')
    exp = Series(exp, dtype='c')
    tm.assert_series_equal(algos.mode(s), exp)
    exp = ['bar']
    data = ['foo'] * 2 + ['bar'] * 3
    for dt in [str, object]:
        s = Series(data, dtype=dt)
        exp = Series(exp, dtype=dt)
        tm.assert_series_equal(algos.mode(s), exp)