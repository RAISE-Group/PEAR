def test_to_period_tz_warning(self):
    ts = Timestamp('2009-04-15 16:17:18', tz='US/Eastern')
    with tm.assert_produces_warning(UserWarning):
        ts.to_period('D')