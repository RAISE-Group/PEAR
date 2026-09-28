def test_number_mode(self):
    exp_single = [1]
    data_single = [1] * 5 + [2] * 3
    exp_multi = [1, 3]
    data_multi = [1] * 5 + [2] * 3 + [3] * 5
    for dt in np.typecodes['AllInteger'] + np.typecodes['Float']:
        s = Series(data_single, dtype=dt)
        exp = Series(exp_single, dtype=dt)
        tm.assert_series_equal(algos.mode(s), exp)
        s = Series(data_multi, dtype=dt)
        exp = Series(exp_multi, dtype=dt)
        tm.assert_series_equal(algos.mode(s), exp)