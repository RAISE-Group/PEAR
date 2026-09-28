def test_td_floordiv_invalid_scalar(self):
    td = Timedelta(hours=3, minutes=4)
    with pytest.raises(TypeError):
        td // np.datetime64('2016-01-01', dtype='datetime64[us]')