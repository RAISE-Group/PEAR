def test_time_loc(self):
    from datetime import time
    from pandas._libs.index import _SIZE_CUTOFF
    ns = _SIZE_CUTOFF + np.array([-100, 100], dtype=np.int64)
    key = time(15, 11, 30)
    start = key.hour * 3600 + key.minute * 60 + key.second
    step = 24 * 3600
    for n in ns:
        idx = pd.date_range('2014-11-26', periods=n, freq='S')
        ts = pd.Series(np.random.randn(n), index=idx)
        i = np.arange(start, n, step)
        tm.assert_numpy_array_equal(ts.index.get_loc(key), i, check_dtype=False)
        tm.assert_series_equal(ts[key], ts.iloc[i])
        left, right = (ts.copy(), ts.copy())
        left[key] *= -10
        right.iloc[i] *= -10
        tm.assert_series_equal(left, right)