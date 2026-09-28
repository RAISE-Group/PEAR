@pytest.mark.parametrize('pos', [0, 1])
@pytest.mark.parametrize('klass,dtype,ctor', [(pd.DatetimeIndex, 'datetime64[ns]', np.datetime64('nat')), (pd.TimedeltaIndex, 'timedelta64[ns]', np.timedelta64('nat'))])
def test_index_ctor_infer_nat_dt_like(self, pos, klass, dtype, ctor, nulls_fixture):
    expected = klass([pd.NaT, pd.NaT])
    assert expected.dtype == dtype
    data = [ctor]
    data.insert(pos, nulls_fixture)
    result = Index(data)
    tm.assert_index_equal(result, expected)
    result = Index(np.array(data, dtype=object))
    tm.assert_index_equal(result, expected)