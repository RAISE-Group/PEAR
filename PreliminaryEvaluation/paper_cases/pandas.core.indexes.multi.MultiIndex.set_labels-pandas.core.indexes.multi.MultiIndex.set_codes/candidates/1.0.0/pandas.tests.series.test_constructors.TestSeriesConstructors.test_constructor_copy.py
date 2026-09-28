def test_constructor_copy(self):
    for data in [[1.0], np.array([1.0])]:
        x = Series(data)
        y = pd.Series(x, copy=True, dtype=float)
        tm.assert_series_equal(x, y)
        x[0] = 2.0
        assert not x.equals(y)
        assert x[0] == 2.0
        assert y[0] == 1.0