def test_constructor_with_nas(self):

    def check(df):
        for i in range(len(df.columns)):
            df.iloc[:, i]
        indexer = np.arange(len(df.columns))[isna(df.columns)]
        if len(indexer) == 0:
            msg = "cannot do label indexing on <class 'pandas\\.core\\.indexes\\.range\\.RangeIndex'> with these indexers \\[nan\\] of <class 'float'>"
            with pytest.raises(TypeError, match=msg):
                df.loc[:, np.nan]
        elif len(indexer) == 1:
            tm.assert_series_equal(df.iloc[:, indexer[0]], df.loc[:, np.nan])
        else:
            tm.assert_frame_equal(df.iloc[:, indexer], df.loc[:, np.nan])
    df = DataFrame([[1, 2, 3], [4, 5, 6]], index=[1, np.nan])
    check(df)
    df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=[1.1, 2.2, np.nan])
    check(df)
    df = DataFrame([[0, 1, 2, 3], [4, 5, 6, 7]], columns=[np.nan, 1.1, 2.2, np.nan])
    check(df)
    df = DataFrame([[0.0, 1, 2, 3.0], [4, 5, 6, 7]], columns=[np.nan, 1.1, 2.2, np.nan])
    check(df)
    df = DataFrame([[0.0, 1, 2, 3.0], [4, 5, 6, 7]], columns=[np.nan, 1, 2, 2])
    check(df)