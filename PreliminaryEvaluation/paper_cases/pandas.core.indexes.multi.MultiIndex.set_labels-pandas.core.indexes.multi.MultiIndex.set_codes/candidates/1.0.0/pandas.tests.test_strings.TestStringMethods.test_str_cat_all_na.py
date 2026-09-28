@pytest.mark.parametrize('other', index_or_series2)
def test_str_cat_all_na(self, index_or_series, other):
    box = index_or_series
    s = Index(['a', 'b', 'c', 'd'])
    s = s if box == Index else Series(s, index=s)
    t = other([np.nan] * 4, dtype=object)
    t = t if other == Index else Series(t, index=s)
    if box == Series:
        expected = Series([np.nan] * 4, index=s.index, dtype=object)
    else:
        expected = Index([np.nan] * 4, dtype=object)
    result = s.str.cat(t, join='left')
    assert_series_or_index_equal(result, expected)
    if other == Series:
        expected = Series([np.nan] * 4, dtype=object, index=t.index)
        result = t.str.cat(s, join='left')
        tm.assert_series_equal(result, expected)