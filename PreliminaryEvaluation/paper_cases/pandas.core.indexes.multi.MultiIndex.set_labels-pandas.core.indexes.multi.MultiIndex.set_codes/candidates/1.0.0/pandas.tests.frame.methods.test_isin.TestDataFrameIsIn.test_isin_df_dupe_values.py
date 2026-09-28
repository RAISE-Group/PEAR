def test_isin_df_dupe_values(self):
    df1 = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]})
    df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['B', 'B'])
    with pytest.raises(ValueError):
        df1.isin(df2)
    df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['A', 'B'], index=[0, 0, 1, 1])
    with pytest.raises(ValueError):
        df1.isin(df2)
    df2.columns = ['B', 'B']
    with pytest.raises(ValueError):
        df1.isin(df2)