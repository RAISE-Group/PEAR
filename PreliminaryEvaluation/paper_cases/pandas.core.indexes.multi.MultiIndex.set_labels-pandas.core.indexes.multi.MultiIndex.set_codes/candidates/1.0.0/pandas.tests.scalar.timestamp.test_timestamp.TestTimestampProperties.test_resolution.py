def test_resolution(self):
    dt = Timestamp('2100-01-01 00:00:00')
    assert dt.resolution == Timedelta(nanoseconds=1)
    assert Timestamp.resolution == Timedelta(nanoseconds=1)