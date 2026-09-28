def test_rolling_median_memory_error(self):
    n = 20000
    Series(np.random.randn(n)).rolling(window=2, center=False).median()
    Series(np.random.randn(n)).rolling(window=2, center=False).median()