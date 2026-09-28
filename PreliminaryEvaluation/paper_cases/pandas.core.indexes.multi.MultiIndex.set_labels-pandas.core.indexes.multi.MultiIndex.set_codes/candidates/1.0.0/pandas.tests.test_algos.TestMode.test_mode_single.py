def test_mode_single(self):
    exp_single = [1]
    data_single = [1]
    exp_multi = [1]
    data_multi = [1, 1]
    for dt in np.typecodes['AllInteger'] + np.typecodes['Float']:
        s = Series(data_single, dtype=dt)
        exp = Series(exp_single, dtype=dt)
        tm.assert_series_equal(algos.mode(s), exp)
        s = Series(data_multi, dtype=dt)
        exp = Series(exp_multi, dtype=dt)
        tm.assert_series_equal(algos.mode(s), exp)
    exp = Series([1], dtype=np.int)
    tm.assert_series_equal(algos.mode([1]), exp)
    exp = Series(['a', 'b', 'c'], dtype=np.object)
    tm.assert_series_equal(algos.mode(['a', 'b', 'c']), exp)