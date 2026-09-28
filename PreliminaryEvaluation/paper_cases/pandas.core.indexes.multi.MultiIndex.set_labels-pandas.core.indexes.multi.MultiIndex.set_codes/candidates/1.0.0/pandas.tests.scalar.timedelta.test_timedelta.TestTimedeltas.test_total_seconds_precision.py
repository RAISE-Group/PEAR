def test_total_seconds_precision(self):
    assert Timedelta('30S').total_seconds() == 30.0
    assert Timedelta('0').total_seconds() == 0.0
    assert Timedelta('-2S').total_seconds() == -2.0
    assert Timedelta('5.324S').total_seconds() == 5.324
    assert Timedelta('30S').total_seconds() - 30.0 < 1e-20
    assert 30.0 - Timedelta('30S').total_seconds() < 1e-20