def test_direct_arith_with_series_returns_not_implemented(self, data):
    other = pd.Series(data)
    result = data.__sub__(other)
    assert result is NotImplemented