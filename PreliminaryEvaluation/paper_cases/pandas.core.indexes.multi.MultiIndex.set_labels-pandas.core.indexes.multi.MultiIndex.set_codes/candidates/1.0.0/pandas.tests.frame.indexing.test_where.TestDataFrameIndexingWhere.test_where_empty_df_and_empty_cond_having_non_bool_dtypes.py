def test_where_empty_df_and_empty_cond_having_non_bool_dtypes(self):
    df = pd.DataFrame(columns=['a'])
    cond = df.applymap(lambda x: x > 0)
    result = df.where(cond)
    tm.assert_frame_equal(result, df)