def test_dups_fancy_indexing2(self):
    df = DataFrame(np.random.randn(5, 5), columns=['A', 'B', 'B', 'B', 'A'])
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[:, ['A', 'B', 'C']]
    df = DataFrame(np.random.randn(9, 2), index=[1, 1, 1, 2, 2, 2, 3, 3, 3], columns=['a', 'b'])
    expected = df.iloc[0:6]
    result = df.loc[[1, 2]]
    tm.assert_frame_equal(result, expected)
    expected = df
    result = df.loc[:, ['a', 'b']]
    tm.assert_frame_equal(result, expected)
    expected = df.iloc[0:6, :]
    result = df.loc[[1, 2], ['a', 'b']]
    tm.assert_frame_equal(result, expected)