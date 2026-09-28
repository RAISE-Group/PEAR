@pytest.mark.parametrize('quantile', [0.0, 0.1, 0.45, 0.5, 1])
@pytest.mark.parametrize('interpolation', ['linear', 'lower', 'higher', 'nearest', 'midpoint'])
@pytest.mark.parametrize('data', [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], [8.0, 1.0, 3.0, 4.0, 5.0, 2.0, 6.0, 7.0], [0.0, np.nan, 0.2, np.nan, 0.4], [np.nan, np.nan, np.nan, np.nan], [np.nan, 0.1, np.nan, 0.3, 0.4, 0.5], [0.5], [np.nan, 0.7, 0.6]])
def test_rolling_quantile_interpolation_options(self, quantile, interpolation, data):
    s = Series(data)
    q1 = s.quantile(quantile, interpolation)
    q2 = s.expanding(min_periods=1).quantile(quantile, interpolation).iloc[-1]
    if np.isnan(q1):
        assert np.isnan(q2)
    else:
        assert q1 == q2