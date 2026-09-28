def test_constructor_tz_or_tzinfo(self):
    stamps = [Timestamp(year=2017, month=10, day=22, tz='UTC'), Timestamp(year=2017, month=10, day=22, tzinfo=utc), Timestamp(year=2017, month=10, day=22, tz=utc), Timestamp(datetime(2017, 10, 22), tzinfo=utc), Timestamp(datetime(2017, 10, 22), tz='UTC'), Timestamp(datetime(2017, 10, 22), tz=utc)]
    assert all((ts == stamps[0] for ts in stamps))