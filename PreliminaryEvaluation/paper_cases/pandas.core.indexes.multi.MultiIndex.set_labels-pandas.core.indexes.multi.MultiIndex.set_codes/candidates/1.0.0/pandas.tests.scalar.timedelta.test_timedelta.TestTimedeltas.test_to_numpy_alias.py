def test_to_numpy_alias(self):
    td = Timedelta('10m7s')
    assert td.to_timedelta64() == td.to_numpy()