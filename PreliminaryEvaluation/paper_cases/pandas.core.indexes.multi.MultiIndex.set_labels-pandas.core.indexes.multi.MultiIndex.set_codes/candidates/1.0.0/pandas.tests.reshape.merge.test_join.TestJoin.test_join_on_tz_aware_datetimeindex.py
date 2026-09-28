def test_join_on_tz_aware_datetimeindex(self):
    df1 = pd.DataFrame({'date': pd.date_range(start='2018-01-01', periods=5, tz='America/Chicago'), 'vals': list('abcde')})
    df2 = pd.DataFrame({'date': pd.date_range(start='2018-01-03', periods=5, tz='America/Chicago'), 'vals_2': list('tuvwx')})
    result = df1.join(df2.set_index('date'), on='date')
    expected = df1.copy()
    expected['vals_2'] = pd.Series([np.nan] * 2 + list('tuv'), dtype=object)
    tm.assert_frame_equal(result, expected)