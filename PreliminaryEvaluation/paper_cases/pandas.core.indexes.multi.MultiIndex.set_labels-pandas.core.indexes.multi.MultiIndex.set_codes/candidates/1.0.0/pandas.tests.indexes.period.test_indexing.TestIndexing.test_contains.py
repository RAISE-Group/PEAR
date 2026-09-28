def test_contains(self):
    p0 = pd.Period('2017-09-01')
    p1 = pd.Period('2017-09-02')
    p2 = pd.Period('2017-09-03')
    p3 = pd.Period('2017-09-04')
    ps0 = [p0, p1, p2]
    idx0 = pd.PeriodIndex(ps0)
    for p in ps0:
        assert p in idx0
        assert str(p) in idx0
    assert '2017-09-01 00:00:01' in idx0
    assert '2017-09' in idx0
    assert p3 not in idx0