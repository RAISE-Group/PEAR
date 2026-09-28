def test_reindex_multi_categorical_time(self):
    midx = pd.MultiIndex.from_product([Categorical(['a', 'b', 'c']), Categorical(date_range('2012-01-01', periods=3, freq='H'))])
    df = pd.DataFrame({'a': range(len(midx))}, index=midx)
    df2 = df.iloc[[0, 1, 2, 3, 4, 5, 6, 8]]
    result = df2.reindex(midx)
    expected = pd.DataFrame({'a': [0, 1, 2, 3, 4, 5, 6, np.nan, 8]}, index=midx)
    tm.assert_frame_equal(result, expected)