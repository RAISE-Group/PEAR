@pytest.mark.parametrize('freq,expected_vals', [('M', [31, 29, 31, 9]), ('2M', [31 + 29, 31 + 9])])
def test_resample_count(self, freq, expected_vals):
    series = Series(1, index=pd.period_range(start='2000', periods=100))
    result = series.resample(freq).count()
    expected_index = pd.period_range(start='2000', freq=freq, periods=len(expected_vals))
    expected = Series(expected_vals, index=expected_index)
    tm.assert_series_equal(result, expected)