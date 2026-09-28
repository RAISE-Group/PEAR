def test_compare_2100(self):
    r = Timestamp('2100-08-12').to_julian_date()
    assert r == 2488292.5