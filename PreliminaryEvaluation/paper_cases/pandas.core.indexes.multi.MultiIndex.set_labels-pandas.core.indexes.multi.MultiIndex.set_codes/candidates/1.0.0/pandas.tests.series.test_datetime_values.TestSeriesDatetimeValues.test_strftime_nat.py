@pytest.mark.parametrize('data', [DatetimeIndex(['2019-01-01', pd.NaT]), PeriodIndex(['2019-01-01', pd.NaT], dtype='period[D]')])
def test_strftime_nat(self, data):
    s = Series(data)
    result = s.dt.strftime('%Y-%m-%d')
    expected = Series(['2019-01-01', np.nan])
    tm.assert_series_equal(result, expected)