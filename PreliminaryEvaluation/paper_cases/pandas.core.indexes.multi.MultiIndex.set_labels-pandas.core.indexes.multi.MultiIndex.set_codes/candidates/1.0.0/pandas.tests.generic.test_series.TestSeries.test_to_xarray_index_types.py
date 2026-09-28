@pytest.mark.skipif(not _XARRAY_INSTALLED or (_XARRAY_INSTALLED and LooseVersion(xarray.__version__) < LooseVersion('0.10.0')), reason='xarray >= 0.10.0 required')
@pytest.mark.parametrize('index', ['FloatIndex', 'IntIndex', 'StringIndex', 'UnicodeIndex', 'DateIndex', 'PeriodIndex', 'TimedeltaIndex', 'CategoricalIndex'])
def test_to_xarray_index_types(self, index):
    from xarray import DataArray
    index = getattr(tm, f'make{index}')
    s = Series(range(6), index=index(6))
    s.index.name = 'foo'
    result = s.to_xarray()
    repr(result)
    assert len(result) == 6
    assert len(result.coords) == 1
    tm.assert_almost_equal(list(result.coords.keys()), ['foo'])
    assert isinstance(result, DataArray)
    tm.assert_series_equal(result.to_series(), s, check_index_type=False, check_categorical=True)