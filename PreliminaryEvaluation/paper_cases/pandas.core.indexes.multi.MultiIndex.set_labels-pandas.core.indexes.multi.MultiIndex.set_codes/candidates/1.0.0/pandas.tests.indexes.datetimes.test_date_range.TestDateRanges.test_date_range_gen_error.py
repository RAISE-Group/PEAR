def test_date_range_gen_error(self):
    rng = date_range('1/1/2000 00:00', '1/1/2000 00:18', freq='5min')
    assert len(rng) == 4