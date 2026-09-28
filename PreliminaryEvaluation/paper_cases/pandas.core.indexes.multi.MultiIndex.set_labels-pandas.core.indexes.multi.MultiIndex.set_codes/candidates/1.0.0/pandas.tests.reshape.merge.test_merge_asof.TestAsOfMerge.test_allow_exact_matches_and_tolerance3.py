def test_allow_exact_matches_and_tolerance3(self):
    df1 = pd.DataFrame({'time': pd.to_datetime(['2016-07-15 13:30:00.030', '2016-07-15 13:30:00.030']), 'username': ['bob', 'charlie']})
    df2 = pd.DataFrame({'time': pd.to_datetime(['2016-07-15 13:30:00.000', '2016-07-15 13:30:00.030']), 'version': [1, 2]})
    result = pd.merge_asof(df1, df2, on='time', allow_exact_matches=False, tolerance=pd.Timedelta('10ms'))
    expected = pd.DataFrame({'time': pd.to_datetime(['2016-07-15 13:30:00.030', '2016-07-15 13:30:00.030']), 'username': ['bob', 'charlie'], 'version': [np.nan, np.nan]})
    tm.assert_frame_equal(result, expected)