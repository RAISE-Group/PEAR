def test_rolling_quantile_param(self):
    ser = Series([0.0, 0.1, 0.5, 0.9, 1.0])
    with pytest.raises(ValueError):
        ser.rolling(3).quantile(-0.1)
    with pytest.raises(ValueError):
        ser.rolling(3).quantile(10.0)
    with pytest.raises(TypeError):
        ser.rolling(3).quantile('foo')