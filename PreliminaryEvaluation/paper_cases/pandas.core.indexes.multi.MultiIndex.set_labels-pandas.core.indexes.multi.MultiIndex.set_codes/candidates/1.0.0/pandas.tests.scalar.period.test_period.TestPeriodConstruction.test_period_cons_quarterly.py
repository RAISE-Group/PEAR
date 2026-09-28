@pytest.mark.parametrize('month', MONTHS)
def test_period_cons_quarterly(self, month):
    freq = 'Q-{month}'.format(month=month)
    exp = Period('1989Q3', freq=freq)
    assert '1989Q3' in str(exp)
    stamp = exp.to_timestamp('D', how='end')
    p = Period(stamp, freq=freq)
    assert p == exp
    stamp = exp.to_timestamp('3D', how='end')
    p = Period(stamp, freq=freq)
    assert p == exp