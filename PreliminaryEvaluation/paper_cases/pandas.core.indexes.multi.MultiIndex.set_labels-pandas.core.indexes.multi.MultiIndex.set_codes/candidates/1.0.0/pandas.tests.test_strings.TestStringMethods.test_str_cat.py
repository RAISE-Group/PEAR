def test_str_cat(self, index_or_series):
    box = index_or_series
    s = box(['a', 'a', 'b', 'b', 'c', np.nan])
    result = s.str.cat()
    expected = 'aabbc'
    assert result == expected
    result = s.str.cat(na_rep='-')
    expected = 'aabbc-'
    assert result == expected
    result = s.str.cat(sep='_', na_rep='NA')
    expected = 'a_a_b_b_c_NA'
    assert result == expected
    t = np.array(['a', np.nan, 'b', 'd', 'foo', np.nan], dtype=object)
    expected = box(['aa', 'a-', 'bb', 'bd', 'cfoo', '--'])
    result = s.str.cat(t, na_rep='-')
    assert_series_or_index_equal(result, expected)
    result = s.str.cat(list(t), na_rep='-')
    assert_series_or_index_equal(result, expected)
    rgx = 'If `others` contains arrays or lists \\(or other list-likes.*'
    z = Series(['1', '2', '3'])
    with pytest.raises(ValueError, match=rgx):
        s.str.cat(z.values)
    with pytest.raises(ValueError, match=rgx):
        s.str.cat(list(z))