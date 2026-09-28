def test_fillna_datelike(self):
    df = DataFrame({'Date': [pd.NaT, Timestamp('2014-1-1')], 'Date2': [Timestamp('2013-1-1'), pd.NaT]})
    expected = df.copy()
    expected['Date'] = expected['Date'].fillna(df.loc[df.index[0], 'Date2'])
    result = df.fillna(value={'Date': df['Date2']})
    tm.assert_frame_equal(result, expected)