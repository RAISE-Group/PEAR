def test_datetime64tz_fillna_round_issue(self):
    data = pd.Series([pd.NaT, pd.NaT, datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc)])
    filled = data.fillna(method='bfill')
    expected = pd.Series([datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc), datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc), datetime(2016, 12, 12, 22, 24, 6, 100001, tzinfo=pytz.utc)])
    tm.assert_series_equal(filled, expected)