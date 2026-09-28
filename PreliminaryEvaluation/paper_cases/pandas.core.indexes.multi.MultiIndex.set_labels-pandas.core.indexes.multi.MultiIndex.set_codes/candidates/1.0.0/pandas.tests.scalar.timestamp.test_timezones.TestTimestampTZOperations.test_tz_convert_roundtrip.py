@pytest.mark.parametrize('stamp', ['2014-02-01 09:00', '2014-07-08 09:00', '2014-11-01 17:00', '2014-11-05 00:00'])
def test_tz_convert_roundtrip(self, stamp, tz_aware_fixture):
    tz = tz_aware_fixture
    ts = Timestamp(stamp, tz='UTC')
    converted = ts.tz_convert(tz)
    reset = converted.tz_convert(None)
    assert reset == Timestamp(stamp)
    assert reset.tzinfo is None
    assert reset == converted.tz_convert('UTC').tz_localize(None)