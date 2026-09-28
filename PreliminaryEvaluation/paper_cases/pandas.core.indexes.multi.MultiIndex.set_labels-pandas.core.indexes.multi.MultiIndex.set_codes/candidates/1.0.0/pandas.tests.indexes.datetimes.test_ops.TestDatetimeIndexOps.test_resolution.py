def test_resolution(self, tz_naive_fixture):
    tz = tz_naive_fixture
    for freq, expected in zip(['A', 'Q', 'M', 'D', 'H', 'T', 'S', 'L', 'U'], ['day', 'day', 'day', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond']):
        idx = pd.date_range(start='2013-04-01', periods=30, freq=freq, tz=tz)
        assert idx.resolution == expected