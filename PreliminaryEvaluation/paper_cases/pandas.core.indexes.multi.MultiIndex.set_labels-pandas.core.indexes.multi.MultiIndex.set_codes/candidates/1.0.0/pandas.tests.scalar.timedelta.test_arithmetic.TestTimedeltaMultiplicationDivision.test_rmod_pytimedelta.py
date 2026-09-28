def test_rmod_pytimedelta(self):
    td = Timedelta(minutes=3)
    result = timedelta(minutes=4) % td
    assert isinstance(result, Timedelta)
    assert result == Timedelta(minutes=1)