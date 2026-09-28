def test_fillna_tzaware_different_column(self):
    df = pd.DataFrame({'A': pd.date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1, 2, np.nan, np.nan]})
    result = df.fillna(method='pad')
    expected = pd.DataFrame({'A': pd.date_range('20130101', periods=4, tz='US/Eastern'), 'B': [1.0, 2.0, 2.0, 2.0]})
    tm.assert_frame_equal(result, expected)