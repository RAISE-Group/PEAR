def test_compare_1700(self):
    r = Timestamp('1700-06-23').to_julian_date()
    assert r == 2342145.5