def test_copy(self):
    for deep in [None, False, True]:
        s = Series(np.arange(10), dtype='float64')
        if deep is None:
            s2 = s.copy()
        else:
            s2 = s.copy(deep=deep)
        s2[::2] = np.NaN
        if deep is None or deep is True:
            assert np.isnan(s2[0])
            assert not np.isnan(s[0])
        else:
            assert np.isnan(s2[0])
            assert np.isnan(s[0])