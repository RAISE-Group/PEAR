def test_reset_index_level(self):
    df = DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=['A', 'B', 'C', 'D'])
    for levels in (['A', 'B'], [0, 1]):
        result = df.set_index(['A', 'B']).reset_index(level=levels[0])
        tm.assert_frame_equal(result, df.set_index('B'))
        result = df.set_index(['A', 'B']).reset_index(level=levels[:1])
        tm.assert_frame_equal(result, df.set_index('B'))
        result = df.set_index(['A', 'B']).reset_index(level=levels)
        tm.assert_frame_equal(result, df)
        result = df.set_index(['A', 'B']).reset_index(level=levels, drop=True)
        tm.assert_frame_equal(result, df[['C', 'D']])
        result = df.set_index('A').reset_index(level=levels[0])
        tm.assert_frame_equal(result, df)
        result = df.set_index('A').reset_index(level=levels[:1])
        tm.assert_frame_equal(result, df)
        result = df.set_index(['A']).reset_index(level=levels[0], drop=True)
        tm.assert_frame_equal(result, df[['B', 'C', 'D']])
    for idx_lev in (['A', 'B'], ['A']):
        with pytest.raises(KeyError, match='(L|l)evel \\(?E\\)?'):
            df.set_index(idx_lev).reset_index(level=['A', 'E'])
        with pytest.raises(IndexError, match='Too many levels'):
            df.set_index(idx_lev).reset_index(level=[0, 1, 2])