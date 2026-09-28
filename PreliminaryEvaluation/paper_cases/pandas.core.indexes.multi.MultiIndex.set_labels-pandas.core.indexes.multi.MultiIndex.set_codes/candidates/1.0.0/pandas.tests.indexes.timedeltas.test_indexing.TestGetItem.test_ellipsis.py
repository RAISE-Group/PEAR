def test_ellipsis(self):
    idx = timedelta_range('1 day', '31 day', freq='D', name='idx')
    result = idx[...]
    assert result.equals(idx)
    assert result is not idx