def test_divmod_ndarray(self, numeric_idx):
    idx = numeric_idx
    other = np.ones(idx.values.shape, dtype=idx.values.dtype) * 2
    result = divmod(idx, other)
    with np.errstate(all='ignore'):
        div, mod = divmod(idx.values, other)
    expected = (Index(div), Index(mod))
    for r, e in zip(result, expected):
        tm.assert_index_equal(r, e)