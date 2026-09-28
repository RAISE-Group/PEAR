def test_td_sub_td(self):
    td = Timedelta(10, unit='d')
    expected = Timedelta(0, unit='ns')
    result = td - td
    assert isinstance(result, Timedelta)
    assert result == expected