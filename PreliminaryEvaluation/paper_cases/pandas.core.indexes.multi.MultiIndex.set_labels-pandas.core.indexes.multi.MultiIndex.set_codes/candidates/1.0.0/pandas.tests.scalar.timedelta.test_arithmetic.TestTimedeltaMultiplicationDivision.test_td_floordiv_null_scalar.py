def test_td_floordiv_null_scalar(self):
    td = Timedelta(hours=3, minutes=4)
    assert td // np.nan is NaT
    assert np.isnan(td // NaT)
    assert np.isnan(td // np.timedelta64('NaT'))