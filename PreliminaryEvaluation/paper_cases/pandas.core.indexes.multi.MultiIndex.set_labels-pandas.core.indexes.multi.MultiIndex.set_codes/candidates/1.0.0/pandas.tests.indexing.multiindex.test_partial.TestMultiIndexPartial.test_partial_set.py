def test_partial_set(self, multiindex_year_month_day_dataframe_random_data):
    ymd = multiindex_year_month_day_dataframe_random_data
    df = ymd.copy()
    exp = ymd.copy()
    df.loc[2000, 4] = 0
    exp.loc[2000, 4].values[:] = 0
    tm.assert_frame_equal(df, exp)
    df['A'].loc[2000, 4] = 1
    exp['A'].loc[2000, 4].values[:] = 1
    tm.assert_frame_equal(df, exp)
    df.loc[2000] = 5
    exp.loc[2000].values[:] = 5
    tm.assert_frame_equal(df, exp)
    df['A'].iloc[14] = 5
    assert df['A'][14] == 5