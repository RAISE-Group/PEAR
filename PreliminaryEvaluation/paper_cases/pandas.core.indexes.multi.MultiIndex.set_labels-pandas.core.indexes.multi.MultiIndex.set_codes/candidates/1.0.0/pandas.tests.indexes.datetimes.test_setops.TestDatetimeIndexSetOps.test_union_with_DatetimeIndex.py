@pytest.mark.parametrize('sort', [None, False])
def test_union_with_DatetimeIndex(self, sort):
    i1 = Int64Index(np.arange(0, 20, 2))
    i2 = date_range(start='2012-01-03 00:00:00', periods=10, freq='D')
    i1.union(i2, sort=sort)
    i2.union(i1, sort=sort)