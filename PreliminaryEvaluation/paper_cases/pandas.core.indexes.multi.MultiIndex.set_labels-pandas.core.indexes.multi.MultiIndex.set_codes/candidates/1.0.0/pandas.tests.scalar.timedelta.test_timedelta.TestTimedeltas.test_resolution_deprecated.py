def test_resolution_deprecated(self):
    td = Timedelta(days=4, hours=3)
    result = td.resolution
    assert result == Timedelta(nanoseconds=1)
    result = Timedelta.resolution
    assert result == Timedelta(nanoseconds=1)