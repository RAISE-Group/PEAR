def test_td_rsub_nat(self):
    td = Timedelta(10, unit='d')
    result = NaT - td
    assert result is NaT
    result = np.datetime64('NaT') - td
    assert result is NaT