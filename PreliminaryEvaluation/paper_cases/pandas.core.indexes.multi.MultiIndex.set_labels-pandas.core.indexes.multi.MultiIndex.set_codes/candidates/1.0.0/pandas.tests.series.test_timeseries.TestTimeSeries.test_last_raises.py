def test_last_raises(self):
    ser = pd.Series('a b c'.split())
    msg = "'last' only supports a DatetimeIndex index"
    with pytest.raises(TypeError, match=msg):
        ser.last('1D')