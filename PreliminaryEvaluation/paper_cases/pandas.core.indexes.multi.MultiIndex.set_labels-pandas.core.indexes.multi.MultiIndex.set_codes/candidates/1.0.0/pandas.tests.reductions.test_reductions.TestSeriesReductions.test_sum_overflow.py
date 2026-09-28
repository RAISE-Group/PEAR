@pytest.mark.parametrize('use_bottleneck', [True, False])
def test_sum_overflow(self, use_bottleneck):
    with pd.option_context('use_bottleneck', use_bottleneck):
        for dtype in ['int32', 'int64']:
            v = np.arange(5000000, dtype=dtype)
            s = Series(v)
            result = s.sum(skipna=False)
            assert int(result) == v.sum(dtype='int64')
            result = s.min(skipna=False)
            assert int(result) == 0
            result = s.max(skipna=False)
            assert int(result) == v[-1]
        for dtype in ['float32', 'float64']:
            v = np.arange(5000000, dtype=dtype)
            s = Series(v)
            result = s.sum(skipna=False)
            assert result == v.sum(dtype=dtype)
            result = s.min(skipna=False)
            assert np.allclose(float(result), 0.0)
            result = s.max(skipna=False)
            assert np.allclose(float(result), v[-1])