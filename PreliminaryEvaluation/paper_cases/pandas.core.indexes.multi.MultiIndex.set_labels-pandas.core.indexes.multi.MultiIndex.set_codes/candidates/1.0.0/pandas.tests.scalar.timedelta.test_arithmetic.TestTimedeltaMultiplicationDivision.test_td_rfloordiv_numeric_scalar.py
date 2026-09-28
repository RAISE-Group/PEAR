def test_td_rfloordiv_numeric_scalar(self):
    td = Timedelta(hours=3, minutes=3)
    assert td.__rfloordiv__(np.nan) is NotImplemented
    assert td.__rfloordiv__(3.5) is NotImplemented
    assert td.__rfloordiv__(2) is NotImplemented
    with pytest.raises(TypeError):
        td.__rfloordiv__(np.float64(2.0))
    with pytest.raises(TypeError):
        td.__rfloordiv__(np.uint8(9))
    with pytest.raises(TypeError, match='Invalid dtype'):
        td.__rfloordiv__(np.int32(2.0))