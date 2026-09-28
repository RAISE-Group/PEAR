def test_searchsorted(self):
    ser = Series([1, 2, 3])
    result = ser.searchsorted(1, side='left')
    assert is_scalar(result)
    assert result == 0
    result = ser.searchsorted(1, side='right')
    assert is_scalar(result)
    assert result == 1