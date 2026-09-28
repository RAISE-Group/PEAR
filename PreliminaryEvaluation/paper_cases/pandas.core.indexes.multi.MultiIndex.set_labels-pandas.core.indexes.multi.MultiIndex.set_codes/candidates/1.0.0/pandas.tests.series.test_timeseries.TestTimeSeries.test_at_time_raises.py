def test_at_time_raises(self):
    ser = pd.Series('a b c'.split())
    msg = 'Index must be DatetimeIndex'
    with pytest.raises(TypeError, match=msg):
        ser.at_time('00:00')