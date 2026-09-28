def test_series_set_tz_timestamp(self, tz_naive_fixture):
    ts = Timestamp('2017-08-05 00:00:00+0100', tz=tz_naive_fixture)
    result = Series(ts)
    result.at[1] = ts
    expected = Series([ts, ts])
    tm.assert_series_equal(result, expected)