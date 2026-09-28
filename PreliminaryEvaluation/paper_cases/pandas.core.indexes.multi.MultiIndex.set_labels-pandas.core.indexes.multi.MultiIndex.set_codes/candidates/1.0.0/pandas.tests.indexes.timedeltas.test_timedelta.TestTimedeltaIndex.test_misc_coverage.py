def test_misc_coverage(self):
    rng = timedelta_range('1 day', periods=5)
    result = rng.groupby(rng.days)
    assert isinstance(list(result.values())[0][0], Timedelta)
    idx = TimedeltaIndex(['3d', '1d', '2d'])
    assert not idx.equals(list(idx))
    non_td = Index(list('abc'))
    assert not idx.equals(list(non_td))