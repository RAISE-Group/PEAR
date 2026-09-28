def test_fillna_datetime_columns(self):
    df = pd.DataFrame({'A': [-1, -2, np.nan], 'B': date_range('20130101', periods=3), 'C': ['foo', 'bar', None], 'D': ['foo2', 'bar2', None]}, index=date_range('20130110', periods=3))
    result = df.fillna('?')
    expected = pd.DataFrame({'A': [-1, -2, '?'], 'B': date_range('20130101', periods=3), 'C': ['foo', 'bar', '?'], 'D': ['foo2', 'bar2', '?']}, index=date_range('20130110', periods=3))
    tm.assert_frame_equal(result, expected)
    df = pd.DataFrame({'A': [-1, -2, np.nan], 'B': [pd.Timestamp('2013-01-01'), pd.Timestamp('2013-01-02'), pd.NaT], 'C': ['foo', 'bar', None], 'D': ['foo2', 'bar2', None]}, index=date_range('20130110', periods=3))
    result = df.fillna('?')
    expected = pd.DataFrame({'A': [-1, -2, '?'], 'B': [pd.Timestamp('2013-01-01'), pd.Timestamp('2013-01-02'), '?'], 'C': ['foo', 'bar', '?'], 'D': ['foo2', 'bar2', '?']}, index=pd.date_range('20130110', periods=3))
    tm.assert_frame_equal(result, expected)