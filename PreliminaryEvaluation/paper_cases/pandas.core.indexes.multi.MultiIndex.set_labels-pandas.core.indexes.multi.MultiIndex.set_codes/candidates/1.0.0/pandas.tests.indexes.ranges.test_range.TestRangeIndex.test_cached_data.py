def test_cached_data(self):
    idx = RangeIndex(0, 100, 10)
    assert idx._cached_data is None
    repr(idx)
    assert idx._cached_data is None
    str(idx)
    assert idx._cached_data is None
    idx.get_loc(20)
    assert idx._cached_data is None
    90 in idx
    assert idx._cached_data is None
    91 in idx
    assert idx._cached_data is None
    idx.all()
    assert idx._cached_data is None
    idx.any()
    assert idx._cached_data is None
    df = pd.DataFrame({'a': range(10)}, index=idx)
    df.loc[50]
    assert idx._cached_data is None
    with pytest.raises(KeyError, match='51'):
        df.loc[51]
    assert idx._cached_data is None
    df.loc[10:50]
    assert idx._cached_data is None
    df.iloc[5:10]
    assert idx._cached_data is None
    assert isinstance(idx._data, np.ndarray)
    assert isinstance(idx._cached_data, np.ndarray)