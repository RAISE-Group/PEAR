def test_constructor_fromordinal(self):
    base = datetime(2000, 1, 1)
    ts = Timestamp.fromordinal(base.toordinal(), freq='D')
    assert base == ts
    assert ts.freq == 'D'
    assert base.toordinal() == ts.toordinal()
    ts = Timestamp.fromordinal(base.toordinal(), tz='US/Eastern')
    assert Timestamp('2000-01-01', tz='US/Eastern') == ts
    assert base.toordinal() == ts.toordinal()
    dt = datetime(2011, 4, 16, 0, 0)
    ts = Timestamp.fromordinal(dt.toordinal())
    assert ts.to_pydatetime() == dt
    stamp = Timestamp('2011-4-16', tz='US/Eastern')
    dt_tz = stamp.to_pydatetime()
    ts = Timestamp.fromordinal(dt_tz.toordinal(), tz='US/Eastern')
    assert ts.to_pydatetime() == dt_tz