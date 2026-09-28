def test_group_var_large_inputs(self):
    prng = RandomState(1234)
    out = np.array([[np.nan]], dtype=self.dtype)
    counts = np.array([0], dtype='int64')
    values = (prng.rand(10 ** 6) + 10 ** 12).astype(self.dtype)
    values.shape = (10 ** 6, 1)
    labels = np.zeros(10 ** 6, dtype='int64')
    self.algo(out, counts, values, labels)
    assert counts[0] == 10 ** 6
    tm.assert_almost_equal(out[0, 0], 1.0 / 12, check_less_precise=True)