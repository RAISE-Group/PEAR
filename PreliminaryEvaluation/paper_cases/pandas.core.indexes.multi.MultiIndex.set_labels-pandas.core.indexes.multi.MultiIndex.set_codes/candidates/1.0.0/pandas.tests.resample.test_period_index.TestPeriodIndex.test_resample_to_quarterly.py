def test_resample_to_quarterly(self, simple_period_range_series):
    for month in MONTHS:
        ts = simple_period_range_series('1990', '1992', freq='A-{month}'.format(month=month))
        quar_ts = ts.resample('Q-{month}'.format(month=month)).ffill()
        stamps = ts.to_timestamp('D', how='start')
        qdates = period_range(ts.index[0].asfreq('D', 'start'), ts.index[-1].asfreq('D', 'end'), freq='Q-{month}'.format(month=month))
        expected = stamps.reindex(qdates.to_timestamp('D', 's'), method='ffill')
        expected.index = qdates
        tm.assert_series_equal(quar_ts, expected)
    ts = simple_period_range_series('1990', '1992', freq='A-JUN')
    for how in ['start', 'end']:
        result = ts.resample('Q-MAR', convention=how).ffill()
        expected = ts.asfreq('Q-MAR', how=how)
        expected = expected.reindex(result.index, method='ffill')
        tm.assert_series_equal(result, expected)