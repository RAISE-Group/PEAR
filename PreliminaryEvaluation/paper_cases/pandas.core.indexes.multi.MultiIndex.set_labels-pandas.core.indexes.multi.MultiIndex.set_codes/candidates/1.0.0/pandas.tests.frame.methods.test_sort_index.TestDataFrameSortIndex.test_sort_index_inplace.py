def test_sort_index_inplace(self):
    frame = DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['A', 'B', 'C', 'D'])
    unordered = frame.loc[[3, 2, 4, 1]]
    a_id = id(unordered['A'])
    df = unordered.copy()
    df.sort_index(inplace=True)
    expected = frame
    tm.assert_frame_equal(df, expected)
    assert a_id != id(df['A'])
    df = unordered.copy()
    df.sort_index(ascending=False, inplace=True)
    expected = frame[::-1]
    tm.assert_frame_equal(df, expected)
    unordered = frame.loc[:, ['D', 'B', 'C', 'A']]
    df = unordered.copy()
    df.sort_index(axis=1, inplace=True)
    expected = frame
    tm.assert_frame_equal(df, expected)
    df = unordered.copy()
    df.sort_index(axis=1, ascending=False, inplace=True)
    expected = frame.iloc[:, ::-1]
    tm.assert_frame_equal(df, expected)