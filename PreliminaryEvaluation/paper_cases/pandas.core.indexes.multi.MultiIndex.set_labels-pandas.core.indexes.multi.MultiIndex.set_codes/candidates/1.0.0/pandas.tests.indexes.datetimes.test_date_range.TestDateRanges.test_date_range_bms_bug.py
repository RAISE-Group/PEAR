def test_date_range_bms_bug(self):
    rng = date_range('1/1/2000', periods=10, freq='BMS')
    ex_first = Timestamp('2000-01-03')
    assert rng[0] == ex_first