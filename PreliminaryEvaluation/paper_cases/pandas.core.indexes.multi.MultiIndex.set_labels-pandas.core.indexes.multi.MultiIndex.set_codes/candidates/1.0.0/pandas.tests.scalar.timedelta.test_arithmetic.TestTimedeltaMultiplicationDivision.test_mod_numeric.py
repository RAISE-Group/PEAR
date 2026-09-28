def test_mod_numeric(self):
    td = Timedelta(hours=37)
    result = td % 2
    assert isinstance(result, Timedelta)
    assert result == Timedelta(0)
    result = td % 1000000000000.0
    assert isinstance(result, Timedelta)
    assert result == Timedelta(minutes=3, seconds=20)
    result = td % int(1000000000000.0)
    assert isinstance(result, Timedelta)
    assert result == Timedelta(minutes=3, seconds=20)