def test_errors(self):
    msg = 'Of the four parameters: start, end, periods, and freq, exactly three must be specified'
    with pytest.raises(ValueError, match=msg):
        timedelta_range(start='0 days')
    with pytest.raises(ValueError, match=msg):
        timedelta_range(end='5 days')
    with pytest.raises(ValueError, match=msg):
        timedelta_range(periods=2)
    with pytest.raises(ValueError, match=msg):
        timedelta_range()
    with pytest.raises(ValueError, match=msg):
        timedelta_range(start='0 days', end='5 days', periods=10, freq='H')