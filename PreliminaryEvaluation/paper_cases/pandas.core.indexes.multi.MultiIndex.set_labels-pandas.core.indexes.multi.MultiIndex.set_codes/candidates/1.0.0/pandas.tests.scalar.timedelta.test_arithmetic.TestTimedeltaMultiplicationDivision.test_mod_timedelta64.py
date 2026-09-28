def test_mod_timedelta64(self):
    td = Timedelta(hours=37)
    result = td % np.timedelta64(2, 'h')
    assert isinstance(result, Timedelta)
    assert result == Timedelta(hours=1)