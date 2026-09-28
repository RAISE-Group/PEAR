def test_joins(self, join_type):
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    joined = index.join(index[:-5], how=join_type)
    assert isinstance(joined, PeriodIndex)
    assert joined.freq == index.freq