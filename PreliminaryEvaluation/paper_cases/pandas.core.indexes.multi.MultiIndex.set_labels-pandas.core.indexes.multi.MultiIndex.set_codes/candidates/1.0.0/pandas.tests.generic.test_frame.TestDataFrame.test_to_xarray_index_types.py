@pytest.mark.skipif(not _XARRAY_INSTALLED or (_XARRAY_INSTALLED and LooseVersion(xarray.__version__) < LooseVersion('0.10.0')), reason='xarray >= 0.10.0 required')
@pytest.mark.parametrize('index', ['FloatIndex', 'IntIndex', 'StringIndex', 'UnicodeIndex', 'DateIndex', 'PeriodIndex', 'CategoricalIndex', 'TimedeltaIndex'])
def test_to_xarray_index_types(self, index):
    from xarray import Dataset
    index = getattr(tm, f'make{index}')
    df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern')})
    df.index = index(3)
    df.index.name = 'foo'
    df.columns.name = 'bar'
    result = df.to_xarray()
    assert result.dims['foo'] == 3
    assert len(result.coords) == 1
    assert len(result.data_vars) == 8
    tm.assert_almost_equal(list(result.coords.keys()), ['foo'])
    assert isinstance(result, Dataset)
    expected = df.copy()
    expected['f'] = expected['f'].astype(object)
    expected.columns.name = None
    tm.assert_frame_equal(result.to_dataframe(), expected, check_index_type=False, check_categorical=False)