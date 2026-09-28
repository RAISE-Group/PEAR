def test_td_rfloordiv_numeric_series(self):
    td = Timedelta(hours=3, minutes=3)
    ser = pd.Series([1], dtype=np.int64)
    res = td.__rfloordiv__(ser)
    assert res is NotImplemented
    with pytest.raises(TypeError, match='Invalid dtype'):
        ser // td