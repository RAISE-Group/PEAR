@pytest.mark.parametrize('data,expected', [(np.array([1, 2, 3, 4, 5], dtype=float), SparseArray(np.array([1.0, 3.0, 6.0, 10.0, 15.0]))), (np.array([1, 2, np.nan, 4, 5], dtype=float), SparseArray(np.array([1.0, 3.0, np.nan, 7.0, 12.0])))])
@pytest.mark.parametrize('numpy', [True, False])
def test_cumsum(self, data, expected, numpy):
    cumsum = np.cumsum if numpy else lambda s: s.cumsum()
    out = cumsum(SparseArray(data))
    tm.assert_sp_array_equal(out, expected)
    out = cumsum(SparseArray(data, fill_value=np.nan))
    tm.assert_sp_array_equal(out, expected)
    out = cumsum(SparseArray(data, fill_value=2))
    tm.assert_sp_array_equal(out, expected)
    if numpy:
        msg = "the 'dtype' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            np.cumsum(SparseArray(data), dtype=np.int64)
        msg = "the 'out' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            np.cumsum(SparseArray(data), out=out)
    else:
        axis = 1
        msg = re.escape(f'axis(={axis}) out of bounds')
        with pytest.raises(ValueError, match=msg):
            SparseArray(data).cumsum(axis=axis)