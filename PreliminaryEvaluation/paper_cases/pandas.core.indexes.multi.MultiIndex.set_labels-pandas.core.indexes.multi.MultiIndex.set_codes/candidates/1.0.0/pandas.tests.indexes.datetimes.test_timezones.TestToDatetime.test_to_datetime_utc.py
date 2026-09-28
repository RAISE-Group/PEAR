def test_to_datetime_utc(self):
    arr = np.array([dateutil.parser.parse('2012-06-13T01:39:00Z')], dtype=object)
    result = to_datetime(arr, utc=True)
    assert result.tz is pytz.utc