def test_rmod_timedelta64(self):
    td = Timedelta(minutes=3)
    result = np.timedelta64(5, 'm') % td
    assert isinstance(result, Timedelta)
    assert result == Timedelta(minutes=2)