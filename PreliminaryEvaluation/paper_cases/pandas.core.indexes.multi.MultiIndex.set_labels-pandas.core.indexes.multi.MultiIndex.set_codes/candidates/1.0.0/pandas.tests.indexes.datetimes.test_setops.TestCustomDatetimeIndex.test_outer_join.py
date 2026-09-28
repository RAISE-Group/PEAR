def test_outer_join(self):
    left = self.rng[:10]
    right = self.rng[5:10]
    the_join = left.join(right, how='outer')
    assert isinstance(the_join, DatetimeIndex)
    left = self.rng[:5]
    right = self.rng[10:]
    the_join = left.join(right, how='outer')
    assert isinstance(the_join, DatetimeIndex)
    assert the_join.freq is None
    left = self.rng[:5]
    right = self.rng[5:10]
    the_join = left.join(right, how='outer')
    assert isinstance(the_join, DatetimeIndex)
    rng = date_range(START, END, freq=BMonthEnd())
    the_join = self.rng.join(rng, how='outer')
    assert isinstance(the_join, DatetimeIndex)
    assert the_join.freq is None