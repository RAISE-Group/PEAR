@pytest.mark.parametrize('op', [operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le])
def test_comparison_tzawareness_compat_scalars(self, op, box_with_array):
    dr = pd.date_range('2016-01-01', periods=6)
    dz = dr.tz_localize('US/Pacific')
    dr = tm.box_expected(dr, box_with_array)
    dz = tm.box_expected(dz, box_with_array)
    ts = pd.Timestamp('2000-03-14 01:59')
    ts_tz = pd.Timestamp('2000-03-14 01:59', tz='Europe/Amsterdam')
    assert np.all(dr > ts)
    msg = 'Cannot compare tz-naive and tz-aware'
    with pytest.raises(TypeError, match=msg):
        op(dr, ts_tz)
    assert np.all(dz > ts_tz)
    with pytest.raises(TypeError, match=msg):
        op(dz, ts)
    with pytest.raises(TypeError, match=msg):
        op(ts, dz)