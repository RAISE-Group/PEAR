def test_freq_setter_errors(self):
    idx = TimedeltaIndex(['0 days', '2 days', '4 days'])
    msg = 'Inferred frequency 2D from passed values does not conform to passed frequency 5D'
    with pytest.raises(ValueError, match=msg):
        idx._data.freq = '5D'
    msg = '<2 \\* BusinessDays> is a non-fixed frequency'
    with pytest.raises(ValueError, match=msg):
        idx._data.freq = '2B'
    with pytest.raises(ValueError, match='Invalid frequency'):
        idx._data.freq = 'foo'