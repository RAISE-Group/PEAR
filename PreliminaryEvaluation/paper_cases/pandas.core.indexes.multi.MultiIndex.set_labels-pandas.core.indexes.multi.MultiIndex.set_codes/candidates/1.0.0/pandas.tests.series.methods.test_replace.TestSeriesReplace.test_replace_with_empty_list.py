def test_replace_with_empty_list(self):
    s = pd.Series([[1], [2, 3], [], np.nan, [4]])
    expected = s
    result = s.replace([], np.nan)
    tm.assert_series_equal(result, expected)
    with pytest.raises(ValueError, match='cannot assign mismatch'):
        s.replace({np.nan: []})
    with pytest.raises(ValueError, match='cannot assign mismatch'):
        s.replace({np.nan: ['dummy', 'alt']})