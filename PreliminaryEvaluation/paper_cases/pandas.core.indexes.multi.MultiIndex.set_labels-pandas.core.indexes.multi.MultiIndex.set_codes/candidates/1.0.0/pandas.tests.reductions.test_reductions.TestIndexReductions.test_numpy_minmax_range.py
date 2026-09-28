def test_numpy_minmax_range(self):
    idx = RangeIndex(0, 10, 3)
    expected = idx._int64index.max()
    result = np.max(idx)
    assert result == expected
    expected = idx._int64index.min()
    result = np.min(idx)
    assert result == expected
    errmsg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=errmsg):
        np.min(idx, out=0)
    with pytest.raises(ValueError, match=errmsg):
        np.max(idx, out=0)