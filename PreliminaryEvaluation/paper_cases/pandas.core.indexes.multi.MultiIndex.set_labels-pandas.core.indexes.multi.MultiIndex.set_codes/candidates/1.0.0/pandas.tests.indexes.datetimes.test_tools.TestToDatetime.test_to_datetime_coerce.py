def test_to_datetime_coerce(self):
    ts_strings = ['March 1, 2018 12:00:00+0400', 'March 1, 2018 12:00:00+0500', '20100240']
    result = to_datetime(ts_strings, errors='coerce')
    expected = Index([datetime(2018, 3, 1, 12, 0, tzinfo=tzoffset(None, 14400)), datetime(2018, 3, 1, 12, 0, tzinfo=tzoffset(None, 18000)), NaT])
    tm.assert_index_equal(result, expected)