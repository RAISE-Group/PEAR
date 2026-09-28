def test_ellipsis(self):
    idx = pd.date_range('2011-01-01', '2011-01-31', freq='D', tz='Asia/Tokyo', name='idx')
    result = idx[...]
    assert result.equals(idx)
    assert result is not idx