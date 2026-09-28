def test_ellipsis(self):
    idx = period_range('2011-01-01', '2011-01-31', freq='D', name='idx')
    result = idx[...]
    assert result.equals(idx)
    assert result is not idx