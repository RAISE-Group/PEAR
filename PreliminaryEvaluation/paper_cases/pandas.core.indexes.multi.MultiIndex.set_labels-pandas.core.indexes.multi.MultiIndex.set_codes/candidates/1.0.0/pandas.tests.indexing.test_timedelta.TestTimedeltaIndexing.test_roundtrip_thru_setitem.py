def test_roundtrip_thru_setitem(self):
    dt1 = pd.Timedelta(0)
    dt2 = pd.Timedelta(28767471428571405)
    df = pd.DataFrame({'dt': pd.Series([dt1, dt2])})
    df_copy = df.copy()
    s = pd.Series([dt1])
    expected = df['dt'].iloc[1].value
    df.loc[[True, False]] = s
    result = df['dt'].iloc[1].value
    assert expected == result
    tm.assert_frame_equal(df, df_copy)