def test_divmod_scalar(self, numeric_idx):
    idx = numeric_idx
    result = divmod(idx, 2)
    with np.errstate(all='ignore'):
        div, mod = divmod(idx.values, 2)
    expected = (Index(div), Index(mod))
    for r, e in zip(result, expected):
        tm.assert_index_equal(r, e)