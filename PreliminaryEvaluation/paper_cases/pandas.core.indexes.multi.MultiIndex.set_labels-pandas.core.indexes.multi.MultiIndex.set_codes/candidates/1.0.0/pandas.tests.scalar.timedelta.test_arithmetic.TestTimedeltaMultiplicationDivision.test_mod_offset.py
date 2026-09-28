def test_mod_offset(self):
    td = Timedelta(hours=37)
    result = td % offsets.Hour(5)
    assert isinstance(result, Timedelta)
    assert result == Timedelta(hours=2)