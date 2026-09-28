def test_dti_drop_dont_lose_tz(self):
    ind = date_range('2012-12-01', periods=10, tz='utc')
    ind = ind.drop(ind[-1])
    assert ind.tz is not None