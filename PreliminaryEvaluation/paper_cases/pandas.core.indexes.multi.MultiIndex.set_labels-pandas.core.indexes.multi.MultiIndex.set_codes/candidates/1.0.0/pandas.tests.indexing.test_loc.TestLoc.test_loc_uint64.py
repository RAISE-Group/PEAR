def test_loc_uint64(self):
    s = pd.Series([1, 2], index=[np.iinfo('uint64').max - 1, np.iinfo('uint64').max])
    result = s.loc[np.iinfo('uint64').max - 1]
    expected = s.iloc[0]
    assert result == expected
    result = s.loc[[np.iinfo('uint64').max - 1]]
    expected = s.iloc[[0]]
    tm.assert_series_equal(result, expected)
    result = s.loc[[np.iinfo('uint64').max - 1, np.iinfo('uint64').max]]
    tm.assert_series_equal(result, s)