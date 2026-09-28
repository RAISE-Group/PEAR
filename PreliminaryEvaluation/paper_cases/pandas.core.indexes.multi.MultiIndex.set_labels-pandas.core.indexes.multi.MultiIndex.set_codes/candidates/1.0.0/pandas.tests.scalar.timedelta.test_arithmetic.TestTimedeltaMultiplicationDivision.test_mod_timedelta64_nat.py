def test_mod_timedelta64_nat(self):
    td = Timedelta(hours=37)
    result = td % np.timedelta64('NaT', 'ns')
    assert result is NaT