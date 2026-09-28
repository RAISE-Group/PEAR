def test_dont_convert_dateutil_utc_to_pytz_utc(self):
    result = Timestamp(datetime(2018, 1, 1), tz=tzutc())
    expected = Timestamp(datetime(2018, 1, 1)).tz_localize(tzutc())
    assert result == expected