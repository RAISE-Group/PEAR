def test_timezone_comparaison_assert(self):
    start = Timestamp('20130220 10:00', tz='US/Eastern')
    msg = 'Inferred time zone not equal to passed time zone'
    with pytest.raises(AssertionError, match=msg):
        date_range(start, periods=2, tz='Europe/Berlin')