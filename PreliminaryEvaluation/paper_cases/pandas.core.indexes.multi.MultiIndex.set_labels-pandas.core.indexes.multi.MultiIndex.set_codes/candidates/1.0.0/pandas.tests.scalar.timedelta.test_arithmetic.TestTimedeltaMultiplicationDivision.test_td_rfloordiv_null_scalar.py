def test_td_rfloordiv_null_scalar(self):
    td = Timedelta(hours=3, minutes=3)
    assert np.isnan(td.__rfloordiv__(NaT))
    assert np.isnan(td.__rfloordiv__(np.timedelta64('NaT')))