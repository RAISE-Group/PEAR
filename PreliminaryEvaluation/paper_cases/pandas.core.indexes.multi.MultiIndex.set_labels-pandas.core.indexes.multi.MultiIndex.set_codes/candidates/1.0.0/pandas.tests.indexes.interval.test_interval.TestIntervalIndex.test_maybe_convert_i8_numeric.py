@pytest.mark.parametrize('breaks', [np.arange(5, dtype='int64'), np.arange(5, dtype='float64')], ids=lambda x: str(x.dtype))
@pytest.mark.parametrize('make_key', [IntervalIndex.from_breaks, lambda breaks: Interval(breaks[0], breaks[1]), lambda breaks: breaks, lambda breaks: breaks[0], list], ids=['IntervalIndex', 'Interval', 'Index', 'scalar', 'list'])
def test_maybe_convert_i8_numeric(self, breaks, make_key):
    index = IntervalIndex.from_breaks(breaks)
    key = make_key(breaks)
    result = index._maybe_convert_i8(key)
    assert result is key