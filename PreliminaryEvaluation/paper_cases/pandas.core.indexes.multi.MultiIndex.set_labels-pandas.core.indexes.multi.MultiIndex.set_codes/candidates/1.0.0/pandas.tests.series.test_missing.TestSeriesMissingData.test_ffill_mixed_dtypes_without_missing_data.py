def test_ffill_mixed_dtypes_without_missing_data(self):
    series = pd.Series([datetime(2015, 1, 1, tzinfo=pytz.utc), 1])
    result = series.ffill()
    tm.assert_series_equal(series, result)