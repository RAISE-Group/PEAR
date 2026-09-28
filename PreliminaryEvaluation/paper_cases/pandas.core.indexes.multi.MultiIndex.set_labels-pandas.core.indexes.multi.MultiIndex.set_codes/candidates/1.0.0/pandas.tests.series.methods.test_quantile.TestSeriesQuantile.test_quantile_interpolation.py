def test_quantile_interpolation(self, datetime_series):
    q = datetime_series.quantile(0.1, interpolation='linear')
    assert q == np.percentile(datetime_series.dropna(), 10)
    q1 = datetime_series.quantile(0.1)
    assert q1 == np.percentile(datetime_series.dropna(), 10)
    assert q == q1