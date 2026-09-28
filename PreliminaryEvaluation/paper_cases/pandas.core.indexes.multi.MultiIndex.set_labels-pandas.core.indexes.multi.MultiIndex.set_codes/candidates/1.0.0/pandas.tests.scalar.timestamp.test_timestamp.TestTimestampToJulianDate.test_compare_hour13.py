def test_compare_hour13(self):
    r = Timestamp('2000-08-12T13:00:00').to_julian_date()
    assert r == 2451769.0416666665