def test_apply_scaler_on_date_time_index_aware_series(self):
    series = tm.makeTimeSeries(nper=30).tz_localize('UTC')
    result = pd.Series(series.index).apply(lambda x: 1)
    tm.assert_series_equal(result, pd.Series(np.ones(30), dtype='int64'))