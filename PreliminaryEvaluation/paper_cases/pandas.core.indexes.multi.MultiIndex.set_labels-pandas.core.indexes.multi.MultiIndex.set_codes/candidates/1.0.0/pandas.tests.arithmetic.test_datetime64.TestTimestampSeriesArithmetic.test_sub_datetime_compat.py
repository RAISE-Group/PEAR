def test_sub_datetime_compat(self):
    s = Series([datetime(2016, 8, 23, 12, tzinfo=pytz.utc), pd.NaT])
    dt = datetime(2016, 8, 22, 12, tzinfo=pytz.utc)
    exp = Series([Timedelta('1 days'), pd.NaT])
    tm.assert_series_equal(s - dt, exp)
    tm.assert_series_equal(s - Timestamp(dt), exp)