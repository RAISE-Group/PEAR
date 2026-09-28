@pytest.mark.parametrize('values', [['0 days', '2 days', '4 days'], []])
@pytest.mark.parametrize('freq', ['2D', Day(2), '48H', Hour(48)])
def test_freq_setter(self, values, freq):
    idx = TimedeltaIndex(values)
    idx._data.freq = freq
    assert idx.freq == freq
    assert isinstance(idx.freq, ABCDateOffset)
    idx._data.freq = None
    assert idx.freq is None