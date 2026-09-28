@pytest.mark.parametrize('freq', ['A', 'Q', 'M', 'W', 'B', 'D'])
def test_asfreq_near_zero(self, freq):
    per = Period('0001-01-01', freq=freq)
    tup1 = (per.year, per.hour, per.day)
    prev = per - 1
    assert prev.ordinal == per.ordinal - 1
    tup2 = (prev.year, prev.month, prev.day)
    assert tup2 < tup1