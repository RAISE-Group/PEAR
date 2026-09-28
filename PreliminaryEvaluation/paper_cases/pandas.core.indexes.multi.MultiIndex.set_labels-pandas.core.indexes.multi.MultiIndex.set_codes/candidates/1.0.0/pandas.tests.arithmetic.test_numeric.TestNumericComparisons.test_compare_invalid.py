def test_compare_invalid(self):
    a = pd.Series(np.random.randn(5), name=0)
    b = pd.Series(np.random.randn(5))
    b.name = pd.Timestamp('2000-01-01')
    tm.assert_series_equal(a / b, 1 / (b / a))