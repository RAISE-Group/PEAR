def test_timezone_comparaison_bug(self):
    start = Timestamp('20130220 10:00', tz='US/Eastern')
    result = date_range(start, periods=2, tz='US/Eastern')
    assert len(result) == 2