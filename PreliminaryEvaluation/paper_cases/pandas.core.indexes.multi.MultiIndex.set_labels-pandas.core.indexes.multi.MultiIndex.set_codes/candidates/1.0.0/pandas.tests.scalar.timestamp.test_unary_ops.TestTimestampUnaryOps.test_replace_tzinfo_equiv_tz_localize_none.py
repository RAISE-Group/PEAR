def test_replace_tzinfo_equiv_tz_localize_none(self):
    ts = Timestamp('2013-11-03 01:59:59.999999-0400', tz='US/Eastern')
    assert ts.tz_localize(None) == ts.replace(tzinfo=None)