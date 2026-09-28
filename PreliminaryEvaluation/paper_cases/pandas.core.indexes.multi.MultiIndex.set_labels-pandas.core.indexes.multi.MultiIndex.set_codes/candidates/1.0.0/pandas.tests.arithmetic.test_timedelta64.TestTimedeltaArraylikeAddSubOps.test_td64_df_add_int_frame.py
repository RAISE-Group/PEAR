def test_td64_df_add_int_frame(self):
    tdi = pd.timedelta_range('1', periods=3)
    df = tdi.to_frame()
    other = pd.DataFrame([1, 2, 3], index=tdi)
    assert_invalid_addsub_type(df, other)