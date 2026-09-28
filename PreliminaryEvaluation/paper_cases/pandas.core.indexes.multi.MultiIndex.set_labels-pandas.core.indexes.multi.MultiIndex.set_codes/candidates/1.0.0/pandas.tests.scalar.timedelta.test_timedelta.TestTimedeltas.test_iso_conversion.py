def test_iso_conversion(self):
    expected = Timedelta(1, unit='s')
    assert to_timedelta('P0DT0H0M1S') == expected