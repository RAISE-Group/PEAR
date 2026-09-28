def test_partial_setting_with_datetimelike_dtype(self):
    df = DataFrame(np.arange(6.0).reshape(3, 2), columns=list('AB'), index=date_range('1/1/2000', periods=3, freq='1H'))
    expected = df.copy()
    expected['C'] = [expected.index[0]] + [pd.NaT, pd.NaT]
    mask = df.A < 1
    df.loc[mask, 'C'] = df.loc[mask].index
    tm.assert_frame_equal(df, expected)