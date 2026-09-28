@td.skip_if_no('xarray', min_version='0.7.0')
def test_to_xarray(self):
    from xarray import DataArray
    s = Series([], dtype=object)
    s.index.name = 'foo'
    result = s.to_xarray()
    assert len(result) == 0
    assert len(result.coords) == 1
    tm.assert_almost_equal(list(result.coords.keys()), ['foo'])
    assert isinstance(result, DataArray)
    s = Series(range(6))
    s.index.name = 'foo'
    s.index = pd.MultiIndex.from_product([['a', 'b'], range(3)], names=['one', 'two'])
    result = s.to_xarray()
    assert len(result) == 2
    tm.assert_almost_equal(list(result.coords.keys()), ['one', 'two'])
    assert isinstance(result, DataArray)
    tm.assert_series_equal(result.to_series(), s)