def test_range_misspecified(self):
    msg = 'Of the four parameters: start, end, periods, and freq, exactly three must be specified'
    with pytest.raises(ValueError, match=msg):
        date_range(start='1/1/2000')
    with pytest.raises(ValueError, match=msg):
        date_range(end='1/1/2000')
    with pytest.raises(ValueError, match=msg):
        date_range(periods=10)
    with pytest.raises(ValueError, match=msg):
        date_range(start='1/1/2000', freq='H')
    with pytest.raises(ValueError, match=msg):
        date_range(end='1/1/2000', freq='H')
    with pytest.raises(ValueError, match=msg):
        date_range(periods=10, freq='H')
    with pytest.raises(ValueError, match=msg):
        date_range()