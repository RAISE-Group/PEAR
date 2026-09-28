def test_getitem_ix_mixed_integer(self):
    df = DataFrame(np.random.randn(4, 3), index=[1, 10, 'C', 'E'], columns=[1, 2, 3])
    result = df.iloc[:-1]
    expected = df.loc[df.index[:-1]]
    tm.assert_frame_equal(result, expected)
    result = df.loc[[1, 10]]
    expected = df.loc[Index([1, 10])]
    tm.assert_frame_equal(result, expected)
    df = pd.DataFrame({'rna': (1.5, 2.2, 3.2, 4.5), -1000: [11, 21, 36, 40], 0: [10, 22, 43, 34], 1000: [0, 10, 20, 30]}, columns=['rna', -1000, 0, 1000])
    result = df[[1000]]
    expected = df.iloc[:, [3]]
    tm.assert_frame_equal(result, expected)
    result = df[[-1000]]
    expected = df.iloc[:, [1]]
    tm.assert_frame_equal(result, expected)