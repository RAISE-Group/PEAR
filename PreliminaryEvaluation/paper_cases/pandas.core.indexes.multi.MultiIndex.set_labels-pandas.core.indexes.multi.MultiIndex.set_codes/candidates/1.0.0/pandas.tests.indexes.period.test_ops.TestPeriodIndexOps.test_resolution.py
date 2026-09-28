def test_resolution(self):
    for freq, expected in zip(['A', 'Q', 'M', 'D', 'H', 'T', 'S', 'L', 'U'], ['day', 'day', 'day', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond']):
        idx = pd.period_range(start='2013-04-01', periods=30, freq=freq)
        assert idx.resolution == expected