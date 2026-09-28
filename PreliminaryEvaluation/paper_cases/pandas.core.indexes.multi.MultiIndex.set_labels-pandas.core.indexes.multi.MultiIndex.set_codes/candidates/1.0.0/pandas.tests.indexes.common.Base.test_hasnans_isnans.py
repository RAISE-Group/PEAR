def test_hasnans_isnans(self, indices):
    if isinstance(indices, MultiIndex):
        return
    idx = indices.copy(deep=True)
    expected = np.array([False] * len(idx), dtype=bool)
    tm.assert_numpy_array_equal(idx._isnan, expected)
    assert idx.hasnans is False
    idx = indices.copy(deep=True)
    values = np.asarray(idx.values)
    if len(indices) == 0:
        return
    elif isinstance(indices, DatetimeIndexOpsMixin):
        values[1] = iNaT
    elif isinstance(indices, (Int64Index, UInt64Index)):
        return
    else:
        values[1] = np.nan
    if isinstance(indices, PeriodIndex):
        idx = type(indices)(values, freq=indices.freq)
    else:
        idx = type(indices)(values)
        expected = np.array([False] * len(idx), dtype=bool)
        expected[1] = True
        tm.assert_numpy_array_equal(idx._isnan, expected)
        assert idx.hasnans is True