def test_reset_index_multiindex_columns(self):
    levels = [['A', ''], ['B', 'b']]
    df = DataFrame([[0, 2], [1, 3]], columns=MultiIndex.from_tuples(levels))
    result = df[['B']].rename_axis('A').reset_index()
    tm.assert_frame_equal(result, df)
    msg = "cannot insert \\('A', ''\\), already exists"
    with pytest.raises(ValueError, match=msg):
        df.rename_axis('A').reset_index()
    result = df.set_index([('A', '')]).reset_index()
    tm.assert_frame_equal(result, df)
    idx_col = DataFrame([[0], [1]], columns=MultiIndex.from_tuples([('level_0', '')]))
    expected = pd.concat([idx_col, df[[('B', 'b'), ('A', '')]]], axis=1)
    result = df.set_index([('B', 'b')], append=True).reset_index()
    tm.assert_frame_equal(result, expected)
    msg = 'Item must have length equal to number of levels.'
    with pytest.raises(ValueError, match=msg):
        df.rename_axis([('C', 'c', 'i')]).reset_index()
    levels = [['A', 'a', ''], ['B', 'b', 'i']]
    df2 = DataFrame([[0, 2], [1, 3]], columns=MultiIndex.from_tuples(levels))
    idx_col = DataFrame([[0], [1]], columns=MultiIndex.from_tuples([('C', 'c', 'ii')]))
    expected = pd.concat([idx_col, df2], axis=1)
    result = df2.rename_axis([('C', 'c')]).reset_index(col_fill='ii')
    tm.assert_frame_equal(result, expected)
    with pytest.raises(ValueError, match="col_fill=None is incompatible with incomplete column name \\('C', 'c'\\)"):
        df2.rename_axis([('C', 'c')]).reset_index(col_fill=None)
    result = df2.rename_axis([('c', 'ii')]).reset_index(col_level=1, col_fill='C')
    tm.assert_frame_equal(result, expected)