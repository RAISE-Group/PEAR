def test_drop_api_equivalence(self):
    df = DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7]], index=['a', 'b', 'c'], columns=['d', 'e', 'f'])
    res1 = df.drop('a')
    res2 = df.drop(index='a')
    tm.assert_frame_equal(res1, res2)
    res1 = df.drop('d', 1)
    res2 = df.drop(columns='d')
    tm.assert_frame_equal(res1, res2)
    res1 = df.drop(labels='e', axis=1)
    res2 = df.drop(columns='e')
    tm.assert_frame_equal(res1, res2)
    res1 = df.drop(['a'], axis=0)
    res2 = df.drop(index=['a'])
    tm.assert_frame_equal(res1, res2)
    res1 = df.drop(['a'], axis=0).drop(['d'], axis=1)
    res2 = df.drop(index=['a'], columns=['d'])
    tm.assert_frame_equal(res1, res2)
    with pytest.raises(ValueError):
        df.drop(labels='a', index='b')
    with pytest.raises(ValueError):
        df.drop(labels='a', columns='b')
    with pytest.raises(ValueError):
        df.drop(axis=1)