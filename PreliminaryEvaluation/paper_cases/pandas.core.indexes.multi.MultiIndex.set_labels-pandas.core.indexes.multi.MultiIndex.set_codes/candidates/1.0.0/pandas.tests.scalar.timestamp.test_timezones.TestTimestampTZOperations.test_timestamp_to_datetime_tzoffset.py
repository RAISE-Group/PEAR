def test_timestamp_to_datetime_tzoffset(self):
    tzinfo = tzoffset(None, 7200)
    expected = Timestamp('3/11/2012 04:00', tz=tzinfo)
    result = Timestamp(expected.to_pydatetime())
    assert expected == result