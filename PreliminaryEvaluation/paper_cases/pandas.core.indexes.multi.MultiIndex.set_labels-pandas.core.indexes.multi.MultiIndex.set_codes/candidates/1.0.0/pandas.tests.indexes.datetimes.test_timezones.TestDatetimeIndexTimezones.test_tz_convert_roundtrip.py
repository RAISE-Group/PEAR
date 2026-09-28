def test_tz_convert_roundtrip(self, tz_aware_fixture):
    tz = tz_aware_fixture
    idx1 = date_range(start='2014-01-01', end='2014-12-31', freq='M', tz='UTC')
    exp1 = date_range(start='2014-01-01', end='2014-12-31', freq='M')
    idx2 = date_range(start='2014-01-01', end='2014-12-31', freq='D', tz='UTC')
    exp2 = date_range(start='2014-01-01', end='2014-12-31', freq='D')
    idx3 = date_range(start='2014-01-01', end='2014-03-01', freq='H', tz='UTC')
    exp3 = date_range(start='2014-01-01', end='2014-03-01', freq='H')
    idx4 = date_range(start='2014-08-01', end='2014-10-31', freq='T', tz='UTC')
    exp4 = date_range(start='2014-08-01', end='2014-10-31', freq='T')
    for idx, expected in [(idx1, exp1), (idx2, exp2), (idx3, exp3), (idx4, exp4)]:
        converted = idx.tz_convert(tz)
        reset = converted.tz_convert(None)
        tm.assert_index_equal(reset, expected)
        assert reset.tzinfo is None
        expected = converted.tz_convert('UTC').tz_localize(None)
        tm.assert_index_equal(reset, expected)