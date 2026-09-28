def test_direct_arith_with_series_returns_not_implemented(self, data):
    other = pd.Series(data)
    if hasattr(data, '__eq__'):
        result = data.__eq__(other)
        assert result is NotImplemented
    else:
        raise pytest.skip(f'{type(data).__name__} does not implement __eq__')