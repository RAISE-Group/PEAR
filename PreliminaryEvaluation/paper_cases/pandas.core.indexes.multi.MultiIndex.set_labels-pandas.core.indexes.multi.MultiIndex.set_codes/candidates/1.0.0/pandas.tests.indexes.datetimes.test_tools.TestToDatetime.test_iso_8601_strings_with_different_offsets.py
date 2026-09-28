def test_iso_8601_strings_with_different_offsets(self):
    ts_strings = ['2015-11-18 15:30:00+05:30', '2015-11-18 16:30:00+06:30', NaT]
    result = to_datetime(ts_strings)
    expected = np.array([datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 19800)), datetime(2015, 11, 18, 16, 30, tzinfo=tzoffset(None, 23400)), NaT], dtype=object)
    expected = Index(expected)
    tm.assert_index_equal(result, expected)
    result = to_datetime(ts_strings, utc=True)
    expected = DatetimeIndex([Timestamp(2015, 11, 18, 10), Timestamp(2015, 11, 18, 10), NaT], tz='UTC')
    tm.assert_index_equal(result, expected)