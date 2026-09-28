def test_iso8601_strings_mixed_offsets_with_naive(self):
    result = pd.to_datetime(['2018-11-28T00:00:00', '2018-11-28T00:00:00+12:00', '2018-11-28T00:00:00', '2018-11-28T00:00:00+06:00', '2018-11-28T00:00:00'], utc=True)
    expected = pd.to_datetime(['2018-11-28T00:00:00', '2018-11-27T12:00:00', '2018-11-28T00:00:00', '2018-11-27T18:00:00', '2018-11-28T00:00:00'], utc=True)
    tm.assert_index_equal(result, expected)
    items = ['2018-11-28T00:00:00+12:00', '2018-11-28T00:00:00']
    result = pd.to_datetime(items, utc=True)
    expected = pd.to_datetime(list(reversed(items)), utc=True)[::-1]
    tm.assert_index_equal(result, expected)