def test_td_div_numeric_scalar(self):
    td = Timedelta(10, unit='d')
    result = td / 2
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=5)
    result = td / 5.0
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=2)