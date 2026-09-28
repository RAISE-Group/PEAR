def test_to_period_microsecond(self):
    index = self.index
    with tm.assert_produces_warning(UserWarning):
        period = index.to_period(freq='U')
    assert 2 == len(period)
    assert period[0] == Period('2007-01-01 10:11:12.123456Z', 'U')
    assert period[1] == Period('2007-01-01 10:11:13.789123Z', 'U')