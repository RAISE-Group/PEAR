@pytest.mark.parametrize('join', ['left', 'outer', 'inner', 'right'])
def test_str_cat_align_mixed_inputs(self, join):
    s = Series(['a', 'b', 'c', 'd'])
    t = Series(['d', 'a', 'e', 'b'], index=[3, 0, 4, 1])
    d = concat([t, t], axis=1)
    expected_outer = Series(['aaa', 'bbb', 'c--', 'ddd', '-ee'])
    expected = expected_outer.loc[s.index.join(t.index, how=join)]
    result = s.str.cat([t, t], join=join, na_rep='-')
    tm.assert_series_equal(result, expected)
    result = s.str.cat(d, join=join, na_rep='-')
    tm.assert_series_equal(result, expected)
    u = np.array(['A', 'B', 'C', 'D'])
    expected_outer = Series(['aaA', 'bbB', 'c-C', 'ddD', '-e-'])
    rhs_idx = t.index & s.index if join == 'inner' else t.index | s.index
    expected = expected_outer.loc[s.index.join(rhs_idx, how=join)]
    result = s.str.cat([t, u], join=join, na_rep='-')
    tm.assert_series_equal(result, expected)
    with pytest.raises(TypeError, match='others must be Series,.*'):
        s.str.cat([t, list(u)], join=join)
    rgx = 'If `others` contains arrays or lists \\(or other list-likes.*'
    z = Series(['1', '2', '3']).values
    with pytest.raises(ValueError, match=rgx):
        s.str.cat(z, join=join)
    with pytest.raises(ValueError, match=rgx):
        s.str.cat([t, z], join=join)