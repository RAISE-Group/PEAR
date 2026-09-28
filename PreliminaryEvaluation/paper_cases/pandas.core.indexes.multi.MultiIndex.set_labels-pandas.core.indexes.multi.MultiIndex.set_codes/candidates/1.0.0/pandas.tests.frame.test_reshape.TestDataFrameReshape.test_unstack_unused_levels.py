def test_unstack_unused_levels(self):
    idx = pd.MultiIndex.from_product([['a'], ['A', 'B', 'C', 'D']])[:-1]
    df = pd.DataFrame([[1, 0]] * 3, index=idx)
    result = df.unstack()
    exp_col = pd.MultiIndex.from_product([[0, 1], ['A', 'B', 'C']])
    expected = pd.DataFrame([[1, 1, 1, 0, 0, 0]], index=['a'], columns=exp_col)
    tm.assert_frame_equal(result, expected)
    assert (result.columns.levels[1] == idx.levels[1]).all()
    levels = [[0, 1, 7], [0, 1, 2, 3]]
    codes = [[0, 0, 1, 1], [0, 2, 0, 2]]
    idx = pd.MultiIndex(levels, codes)
    block = np.arange(4).reshape(2, 2)
    df = pd.DataFrame(np.concatenate([block, block + 4]), index=idx)
    result = df.unstack()
    expected = pd.DataFrame(np.concatenate([block * 2, block * 2 + 1], axis=1), columns=idx)
    tm.assert_frame_equal(result, expected)
    assert (result.columns.levels[1] == idx.levels[1]).all()
    levels = [['a', 2, 'c'], [1, 3, 5, 7]]
    codes = [[0, -1, 1, 1], [0, 2, -1, 2]]
    idx = pd.MultiIndex(levels, codes)
    data = np.arange(8)
    df = pd.DataFrame(data.reshape(4, 2), index=idx)
    cases = ((0, [13, 16, 6, 9, 2, 5, 8, 11], [np.nan, 'a', 2], [np.nan, 5, 1]), (1, [8, 11, 1, 4, 12, 15, 13, 16], [np.nan, 5, 1], [np.nan, 'a', 2]))
    for level, idces, col_level, idx_level in cases:
        result = df.unstack(level=level)
        exp_data = np.zeros(18) * np.nan
        exp_data[idces] = data
        cols = pd.MultiIndex.from_product([[0, 1], col_level])
        expected = pd.DataFrame(exp_data.reshape(3, 6), index=idx_level, columns=cols)
        tm.assert_frame_equal(result, expected)