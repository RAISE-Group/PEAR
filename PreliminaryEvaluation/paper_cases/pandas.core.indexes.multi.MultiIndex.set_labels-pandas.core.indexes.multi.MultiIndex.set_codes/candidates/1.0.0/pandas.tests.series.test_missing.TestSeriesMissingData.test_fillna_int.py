def test_fillna_int(self):
    s = Series(np.random.randint(-100, 100, 50))
    s.fillna(method='ffill', inplace=True)
    tm.assert_series_equal(s.fillna(method='ffill', inplace=False), s)