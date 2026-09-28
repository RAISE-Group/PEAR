def test_misc_coverage(self):
    rng = date_range('1/1/2000', periods=5)
    result = rng.groupby(rng.day)
    assert isinstance(list(result.values())[0][0], Timestamp)
    idx = DatetimeIndex(['2000-01-03', '2000-01-01', '2000-01-02'])
    assert not idx.equals(list(idx))
    non_datetime = Index(list('abc'))
    assert not idx.equals(list(non_datetime))