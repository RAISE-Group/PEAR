def test_round_tzaware(self):
    dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
    result = dt.round('D')
    expected = Timestamp('20130101', tz='US/Eastern')
    assert result == expected
    dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
    result = dt.round('s')
    assert result == dt