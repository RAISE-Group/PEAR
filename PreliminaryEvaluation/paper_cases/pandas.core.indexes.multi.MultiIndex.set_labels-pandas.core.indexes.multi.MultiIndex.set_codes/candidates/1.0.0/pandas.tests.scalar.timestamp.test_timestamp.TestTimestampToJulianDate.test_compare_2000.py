def test_compare_2000(self):
    r = Timestamp('2000-04-12').to_julian_date()
    assert r == 2451646.5