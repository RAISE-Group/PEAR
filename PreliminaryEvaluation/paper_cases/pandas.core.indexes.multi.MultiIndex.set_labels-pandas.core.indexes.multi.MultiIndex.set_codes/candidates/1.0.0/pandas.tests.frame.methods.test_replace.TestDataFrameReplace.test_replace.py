def test_replace(self, datetime_frame):
    datetime_frame['A'][:5] = np.nan
    datetime_frame['A'][-5:] = np.nan
    zero_filled = datetime_frame.replace(np.nan, -100000000.0)
    tm.assert_frame_equal(zero_filled, datetime_frame.fillna(-100000000.0))
    tm.assert_frame_equal(zero_filled.replace(-100000000.0, np.nan), datetime_frame)
    datetime_frame['A'][:5] = np.nan
    datetime_frame['A'][-5:] = np.nan
    datetime_frame['B'][:5] = -100000000.0
    df = DataFrame(index=['a', 'b'])
    tm.assert_frame_equal(df, df.replace(5, 7))
    df = pd.DataFrame([('-', pd.to_datetime('20150101')), ('a', pd.to_datetime('20150102'))])
    df1 = df.replace('-', np.nan)
    expected_df = pd.DataFrame([(np.nan, pd.to_datetime('20150101')), ('a', pd.to_datetime('20150102'))])
    tm.assert_frame_equal(df1, expected_df)