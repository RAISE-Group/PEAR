def test_td_sub_offset(self):
    td = Timedelta(10, unit='d')
    result = td - offsets.Hour(1)
    assert isinstance(result, Timedelta)
    assert result == Timedelta(239, unit='h')