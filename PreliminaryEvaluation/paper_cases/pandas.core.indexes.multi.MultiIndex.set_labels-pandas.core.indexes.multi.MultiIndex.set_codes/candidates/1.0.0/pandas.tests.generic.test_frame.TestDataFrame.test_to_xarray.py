@td.skip_if_no('xarray', min_version='0.7.0')
def test_to_xarray(self):
    from xarray import Dataset
    df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.Categorical(list('abc')), 'g': pd.date_range('20130101', periods=3), 'h': pd.date_range('20130101', periods=3, tz='US/Eastern')})
    df.index.name = 'foo'
    result = df[0:0].to_xarray()
    assert result.dims['foo'] == 0
    assert isinstance(result, Dataset)
    df.index = pd.MultiIndex.from_product([['a'], range(3)], names=['one', 'two'])
    result = df.to_xarray()
    assert result.dims['one'] == 1
    assert result.dims['two'] == 3
    assert len(result.coords) == 2
    assert len(result.data_vars) == 8
    tm.assert_almost_equal(list(result.coords.keys()), ['one', 'two'])
    assert isinstance(result, Dataset)
    result = result.to_dataframe()
    expected = df.copy()
    expected['f'] = expected['f'].astype(object)
    expected.columns.name = None
    tm.assert_frame_equal(result, expected, check_index_type=False)