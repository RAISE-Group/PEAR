@pytest.mark.parametrize('op', [operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le])
def test_comparison_tzawareness_compat(self, op, box_df_fail):
    box = box_df_fail
    dr = pd.date_range('2016-01-01', periods=6)
    dz = dr.tz_localize('US/Pacific')
    dr = tm.box_expected(dr, box)
    dz = tm.box_expected(dz, box)
    msg = 'Cannot compare tz-naive and tz-aware'
    with pytest.raises(TypeError, match=msg):
        op(dr, dz)
    with pytest.raises(TypeError, match=msg):
        op(dr, list(dz))
    with pytest.raises(TypeError, match=msg):
        op(dr, np.array(list(dz), dtype=object))
    with pytest.raises(TypeError, match=msg):
        op(dz, dr)
    with pytest.raises(TypeError, match=msg):
        op(dz, list(dr))
    with pytest.raises(TypeError, match=msg):
        op(dz, np.array(list(dr), dtype=object))
    assert np.all(dr == dr)
    assert np.all(dr == list(dr))
    assert np.all(list(dr) == dr)
    assert np.all(np.array(list(dr), dtype=object) == dr)
    assert np.all(dr == np.array(list(dr), dtype=object))
    assert np.all(dz == dz)
    assert np.all(dz == list(dz))
    assert np.all(list(dz) == dz)
    assert np.all(np.array(list(dz), dtype=object) == dz)
    assert np.all(dz == np.array(list(dz), dtype=object))