def test_non_iso_strings_with_tz_offset(self):
    result = to_datetime(['March 1, 2018 12:00:00+0400'] * 2)
    expected = DatetimeIndex([datetime(2018, 3, 1, 12, tzinfo=pytz.FixedOffset(240))] * 2)
    tm.assert_index_equal(result, expected)