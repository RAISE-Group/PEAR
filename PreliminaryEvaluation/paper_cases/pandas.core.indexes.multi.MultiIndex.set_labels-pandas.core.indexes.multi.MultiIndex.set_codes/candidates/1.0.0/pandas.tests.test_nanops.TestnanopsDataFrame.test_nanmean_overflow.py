def test_nanmean_overflow(self):
    for a in [2 ** 55, -2 ** 55, 20150515061816532]:
        s = Series(a, index=range(500), dtype=np.int64)
        result = s.mean()
        np_result = s.values.mean()
        assert result == a
        assert result == np_result
        assert result.dtype == np.float64