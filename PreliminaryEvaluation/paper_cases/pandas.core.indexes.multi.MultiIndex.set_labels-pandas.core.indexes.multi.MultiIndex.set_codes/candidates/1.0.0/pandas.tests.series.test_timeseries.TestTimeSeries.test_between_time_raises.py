def test_between_time_raises(self):
    ser = pd.Series('a b c'.split())
    msg = 'Index must be DatetimeIndex'
    with pytest.raises(TypeError, match=msg):
        ser.between_time(start_time='00:00', end_time='12:00')