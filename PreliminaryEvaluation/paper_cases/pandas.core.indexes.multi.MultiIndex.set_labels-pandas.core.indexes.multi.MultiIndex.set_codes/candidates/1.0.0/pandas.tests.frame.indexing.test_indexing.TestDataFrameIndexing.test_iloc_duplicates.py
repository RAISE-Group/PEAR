def test_iloc_duplicates(self):
    df = DataFrame(np.random.rand(3, 3), columns=list('ABC'), index=list('aab'))
    result = df.iloc[0]
    assert isinstance(result, Series)
    tm.assert_almost_equal(result.values, df.values[0])
    result = df.T.iloc[:, 0]
    assert isinstance(result, Series)
    tm.assert_almost_equal(result.values, df.values[0])
    df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=[1, 1, 2])
    result = df.iloc[:, [0]]
    expected = df.take([0], axis=1)
    tm.assert_frame_equal(result, expected)