def test_properties_annually(self):
    a_date = Period(freq='A', year=2007)
    assert a_date.year == 2007