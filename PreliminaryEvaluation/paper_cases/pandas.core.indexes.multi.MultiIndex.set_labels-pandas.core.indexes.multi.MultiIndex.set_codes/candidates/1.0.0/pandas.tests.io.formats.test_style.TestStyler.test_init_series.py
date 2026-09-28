def test_init_series(self):
    result = Styler(pd.Series([1, 2]))
    assert result.data.ndim == 2