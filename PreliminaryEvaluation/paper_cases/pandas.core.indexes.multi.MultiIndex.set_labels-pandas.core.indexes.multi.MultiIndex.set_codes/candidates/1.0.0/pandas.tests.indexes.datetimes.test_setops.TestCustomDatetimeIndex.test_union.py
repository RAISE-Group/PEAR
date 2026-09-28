@pytest.mark.parametrize('sort', [None, False])
def test_union(self, sort):
    left = self.rng[:10]
    right = self.rng[5:10]
    the_union = left.union(right, sort=sort)
    assert isinstance(the_union, DatetimeIndex)
    left = self.rng[:5]
    right = self.rng[10:]
    the_union = left.union(right, sort)
    assert isinstance(the_union, Index)
    left = self.rng[:5]
    right = self.rng[5:10]
    the_union = left.union(right, sort=sort)
    assert isinstance(the_union, DatetimeIndex)
    if sort is None:
        tm.assert_index_equal(right.union(left, sort=sort), the_union)
    rng = date_range(START, END, freq=BMonthEnd())
    the_union = self.rng.union(rng, sort=sort)
    assert isinstance(the_union, DatetimeIndex)