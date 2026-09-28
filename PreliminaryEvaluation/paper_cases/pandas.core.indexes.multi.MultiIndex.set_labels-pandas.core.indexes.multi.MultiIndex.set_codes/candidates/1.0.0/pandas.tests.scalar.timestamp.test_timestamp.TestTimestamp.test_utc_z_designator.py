def test_utc_z_designator(self):
    assert get_timezone(Timestamp('2014-11-02 01:00Z').tzinfo) is utc