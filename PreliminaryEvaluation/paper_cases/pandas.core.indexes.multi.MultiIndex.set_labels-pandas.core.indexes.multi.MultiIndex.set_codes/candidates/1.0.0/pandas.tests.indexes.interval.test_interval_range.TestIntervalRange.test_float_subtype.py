@pytest.mark.parametrize('freq', [2, 2.0])
@pytest.mark.parametrize('end', [10, 10.0])
@pytest.mark.parametrize('start', [0, 0.0])
def test_float_subtype(self, start, end, freq):
    index = interval_range(start=start, end=end, freq=freq)
    result = index.dtype.subtype
    expected = 'int64' if is_integer(start + end + freq) else 'float64'
    assert result == expected
    index = interval_range(start=start, periods=5, freq=freq)
    result = index.dtype.subtype
    expected = 'int64' if is_integer(start + freq) else 'float64'
    assert result == expected
    index = interval_range(end=end, periods=5, freq=freq)
    result = index.dtype.subtype
    expected = 'int64' if is_integer(end + freq) else 'float64'
    assert result == expected
    index = interval_range(start=start, end=end, periods=5)
    result = index.dtype.subtype
    expected = 'int64' if is_integer(start + end) else 'float64'
    assert result == expected