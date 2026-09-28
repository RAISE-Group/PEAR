def test_td_sub_nat(self):
    td = Timedelta(10, unit='d')
    result = td - NaT
    assert result is NaT