@pytest.mark.parametrize('value', [None, pd.NaT, np.nan])
def test_masked_setitem(self, value):
    series = pd.Series([0, 1, 2], dtype='timedelta64[ns]')
    series[series == series[0]] = value
    expected = pd.Series([pd.NaT, 1, 2], dtype='timedelta64[ns]')
    tm.assert_series_equal(series, expected)