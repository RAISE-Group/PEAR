def test_group_var_generic_2d_all_finite(self):
    prng = RandomState(1234)
    out = (np.nan * np.ones((5, 2))).astype(self.dtype)
    counts = np.zeros(5, dtype='int64')
    values = 10 * prng.rand(10, 2).astype(self.dtype)
    labels = np.tile(np.arange(5), (2,)).astype('int64')
    expected_out = np.std(values.reshape(2, 5, 2), ddof=1, axis=0) ** 2
    expected_counts = counts + 2
    self.algo(out, counts, values, labels)
    assert np.allclose(out, expected_out, self.rtol)
    tm.assert_numpy_array_equal(counts, expected_counts)