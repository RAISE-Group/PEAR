def test_deprecate_order(self):
    data = np.array([2 ** 63, 1, 2 ** 63], dtype=np.uint64)
    with pytest.raises(TypeError, match='got an unexpected keyword'):
        algos.factorize(data, order=True)
    with tm.assert_produces_warning(False):
        algos.factorize(data)