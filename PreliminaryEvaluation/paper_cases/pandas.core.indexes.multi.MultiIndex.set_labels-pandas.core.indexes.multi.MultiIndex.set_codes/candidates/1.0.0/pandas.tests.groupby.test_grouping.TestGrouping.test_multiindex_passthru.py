def test_multiindex_passthru(self):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df.columns = pd.MultiIndex.from_tuples([(0, 1), (1, 1), (2, 1)])
    result = df.groupby(axis=1, level=[0, 1]).first()
    tm.assert_frame_equal(result, df)