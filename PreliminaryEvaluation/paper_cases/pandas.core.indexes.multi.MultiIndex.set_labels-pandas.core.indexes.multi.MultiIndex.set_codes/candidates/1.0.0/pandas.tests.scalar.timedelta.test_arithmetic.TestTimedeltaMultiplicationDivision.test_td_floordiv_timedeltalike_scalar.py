def test_td_floordiv_timedeltalike_scalar(self):
    td = Timedelta(hours=3, minutes=4)
    scalar = Timedelta(hours=3, minutes=3)
    assert td // scalar == 1
    assert -td // scalar.to_pytimedelta() == -2
    assert 2 * td // scalar.to_timedelta64() == 2