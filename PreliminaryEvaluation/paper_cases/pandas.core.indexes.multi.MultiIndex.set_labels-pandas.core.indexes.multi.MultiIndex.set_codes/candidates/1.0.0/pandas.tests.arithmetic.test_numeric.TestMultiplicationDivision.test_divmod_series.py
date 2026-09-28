def test_divmod_series(self, numeric_idx):
    idx = numeric_idx
    other = np.ones(idx.values.shape, dtype=idx.values.dtype) * 2
    result = divmod(idx, Series(other))
    with np.errstate(all='ignore'):
        div, mod = divmod(idx.values, other)
    expected = (Series(div), Series(mod))
    for r, e in zip(result, expected):
        tm.assert_series_equal(r, e)