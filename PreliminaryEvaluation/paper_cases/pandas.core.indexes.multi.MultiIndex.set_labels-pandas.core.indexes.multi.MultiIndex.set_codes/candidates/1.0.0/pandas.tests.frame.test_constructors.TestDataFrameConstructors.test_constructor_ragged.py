def test_constructor_ragged(self):
    data = {'A': np.random.randn(10), 'B': np.random.randn(8)}
    with pytest.raises(ValueError, match='arrays must all be same length'):
        DataFrame(data)