def test_df_add_td64_columnwise(self):
    dti = pd.date_range('2016-01-01', periods=10)
    tdi = pd.timedelta_range('1', periods=10)
    tser = pd.Series(tdi)
    df = pd.DataFrame({0: dti, 1: tdi})
    result = df.add(tser, axis=0)
    expected = pd.DataFrame({0: dti + tdi, 1: tdi + tdi})
    tm.assert_frame_equal(result, expected)