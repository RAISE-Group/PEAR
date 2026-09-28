def test_first_raises(self):
    ser = pd.Series('a b c'.split())
    msg = "'first' only supports a DatetimeIndex index"
    with pytest.raises(TypeError, match=msg):
        ser.first('1D')