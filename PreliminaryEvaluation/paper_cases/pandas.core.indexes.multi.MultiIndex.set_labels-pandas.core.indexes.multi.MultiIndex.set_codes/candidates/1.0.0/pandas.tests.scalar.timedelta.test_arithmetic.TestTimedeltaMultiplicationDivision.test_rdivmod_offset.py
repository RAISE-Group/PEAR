def test_rdivmod_offset(self):
    result = divmod(offsets.Hour(54), Timedelta(hours=-4))
    assert result[0] == -14
    assert isinstance(result[1], Timedelta)
    assert result[1] == Timedelta(hours=-2)