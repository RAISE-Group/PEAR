def test_datetime_timedelta_quantiles(self):
    assert pd.isna(Series([], dtype='M8[ns]').quantile(0.5))
    assert pd.isna(Series([], dtype='m8[ns]').quantile(0.5))