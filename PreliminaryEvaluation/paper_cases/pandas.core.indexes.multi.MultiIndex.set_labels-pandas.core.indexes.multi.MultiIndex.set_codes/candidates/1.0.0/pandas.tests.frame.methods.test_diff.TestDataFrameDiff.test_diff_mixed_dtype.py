def test_diff_mixed_dtype(self):
    df = DataFrame(np.random.randn(5, 3))
    df['A'] = np.array([1, 2, 3, 4, 5], dtype=object)
    result = df.diff()
    assert result[0].dtype == np.float64