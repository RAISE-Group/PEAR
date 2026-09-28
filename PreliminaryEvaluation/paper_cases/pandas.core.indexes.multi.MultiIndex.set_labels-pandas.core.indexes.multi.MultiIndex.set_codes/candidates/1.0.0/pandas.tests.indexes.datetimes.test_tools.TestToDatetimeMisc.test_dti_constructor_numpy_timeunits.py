@pytest.mark.parametrize('dtype', ['datetime64[h]', 'datetime64[m]', 'datetime64[s]', 'datetime64[ms]', 'datetime64[us]', 'datetime64[ns]'])
@pytest.mark.parametrize('cache', [True, False])
def test_dti_constructor_numpy_timeunits(self, cache, dtype):
    base = pd.to_datetime(['2000-01-01T00:00', '2000-01-02T00:00', 'NaT'], cache=cache)
    values = base.values.astype(dtype)
    tm.assert_index_equal(DatetimeIndex(values), base)
    tm.assert_index_equal(to_datetime(values, cache=cache), base)