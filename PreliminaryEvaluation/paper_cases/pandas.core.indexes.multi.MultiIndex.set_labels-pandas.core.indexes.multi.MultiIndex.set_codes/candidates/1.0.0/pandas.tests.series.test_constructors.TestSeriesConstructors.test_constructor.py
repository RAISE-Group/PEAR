def test_constructor(self, datetime_series):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        empty_series = Series()
    assert datetime_series.index.is_all_dates
    derived = Series(datetime_series)
    assert derived.index.is_all_dates
    assert tm.equalContents(derived.index, datetime_series.index)
    assert id(datetime_series.index) == id(derived.index)
    mixed = Series(['hello', np.NaN], index=[0, 1])
    assert mixed.dtype == np.object_
    assert mixed[1] is np.NaN
    assert not empty_series.index.is_all_dates
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        assert not Series().index.is_all_dates
    with pytest.raises(Exception, match='Data must be 1-dimensional'):
        Series(np.random.randn(3, 3), index=np.arange(3))
    mixed.name = 'Series'
    rs = Series(mixed).name
    xp = 'Series'
    assert rs == xp
    m = MultiIndex.from_arrays([[1, 2], [3, 4]])
    msg = 'initializing a Series from a MultiIndex is not supported'
    with pytest.raises(NotImplementedError, match=msg):
        Series(m)