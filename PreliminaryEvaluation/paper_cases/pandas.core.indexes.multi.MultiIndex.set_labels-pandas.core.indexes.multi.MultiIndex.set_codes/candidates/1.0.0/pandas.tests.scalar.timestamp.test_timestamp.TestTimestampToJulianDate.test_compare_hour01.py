def test_compare_hour01(self):
    r = Timestamp('2000-08-12T01:00:00').to_julian_date()
    assert r == 2451768.5416666665