def test_factorize_tz(self, tz_naive_fixture):
    tz = tz_naive_fixture
    base = pd.date_range('2016-11-05', freq='H', periods=100, tz=tz)
    idx = base.repeat(5)
    exp_arr = np.arange(100, dtype=np.intp).repeat(5)
    for obj in [idx, pd.Series(idx)]:
        arr, res = obj.factorize()
        tm.assert_numpy_array_equal(arr, exp_arr)
        tm.assert_index_equal(res, base)