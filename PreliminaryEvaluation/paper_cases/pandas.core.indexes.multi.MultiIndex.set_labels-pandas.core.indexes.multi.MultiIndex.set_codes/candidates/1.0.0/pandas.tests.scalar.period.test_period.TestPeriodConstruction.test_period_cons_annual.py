@pytest.mark.parametrize('month', MONTHS)
def test_period_cons_annual(self, month):
    freq = 'A-{month}'.format(month=month)
    exp = Period('1989', freq=freq)
    stamp = exp.to_timestamp('D', how='end') + timedelta(days=30)
    p = Period(stamp, freq=freq)
    assert p == exp + 1
    assert isinstance(p, Period)