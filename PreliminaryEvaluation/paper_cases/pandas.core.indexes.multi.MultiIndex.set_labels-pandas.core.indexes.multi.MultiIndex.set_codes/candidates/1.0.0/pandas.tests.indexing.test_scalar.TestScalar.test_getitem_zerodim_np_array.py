def test_getitem_zerodim_np_array(self):
    df = DataFrame([[1, 2], [3, 4]])
    result = df[np.array(0)]
    expected = Series([1, 3], name=0)
    tm.assert_series_equal(result, expected)
    s = Series([1, 2])
    result = s[np.array(0)]
    assert result == 1