def test_td_rfloordiv_invalid_scalar(self):
    td = Timedelta(hours=3, minutes=3)
    dt64 = np.datetime64('2016-01-01', 'us')
    with pytest.raises(TypeError):
        td.__rfloordiv__(dt64)