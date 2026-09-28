@pytest.mark.parametrize('day', DAYS)
@pytest.mark.parametrize('num', range(10, 17))
def test_period_cons_weekly(self, num, day):
    daystr = '2011-02-{num}'.format(num=num)
    freq = 'W-{day}'.format(day=day)
    result = Period(daystr, freq=freq)
    expected = Period(daystr, freq='D').asfreq(freq)
    assert result == expected
    assert isinstance(result, Period)