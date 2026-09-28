def test_mod_timedeltalike(self):
    td = Timedelta(hours=37)
    result = td % Timedelta(hours=6)
    assert isinstance(result, Timedelta)
    assert result == Timedelta(hours=1)
    result = td % timedelta(minutes=60)
    assert isinstance(result, Timedelta)
    assert result == Timedelta(0)
    result = td % NaT
    assert result is NaT