def test_apply_simple_series(self, data):
    result = pd.Series(data).apply(id)
    assert isinstance(result, pd.Series)