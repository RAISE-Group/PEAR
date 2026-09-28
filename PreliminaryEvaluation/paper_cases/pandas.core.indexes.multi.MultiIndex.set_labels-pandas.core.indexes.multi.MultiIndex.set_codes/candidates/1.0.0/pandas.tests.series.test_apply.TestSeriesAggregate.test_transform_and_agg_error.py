def test_transform_and_agg_error(self, string_series):
    with pytest.raises(ValueError):
        string_series.transform(['min', 'max'])
    with pytest.raises(ValueError):
        with np.errstate(all='ignore'):
            string_series.agg(['sqrt', 'max'])
    with pytest.raises(ValueError):
        with np.errstate(all='ignore'):
            string_series.transform(['sqrt', 'max'])
    with pytest.raises(ValueError):
        with np.errstate(all='ignore'):
            string_series.agg({'foo': np.sqrt, 'bar': 'sum'})