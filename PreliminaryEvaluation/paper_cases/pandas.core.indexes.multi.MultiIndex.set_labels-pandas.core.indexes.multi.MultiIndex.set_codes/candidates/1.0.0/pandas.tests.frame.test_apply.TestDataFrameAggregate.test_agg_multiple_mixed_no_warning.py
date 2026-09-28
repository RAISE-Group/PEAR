def test_agg_multiple_mixed_no_warning(self):
    mdf = pd.DataFrame({'A': [1, 2, 3], 'B': [1.0, 2.0, 3.0], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20130101', periods=3)})
    expected = pd.DataFrame({'A': [1, 6], 'B': [1.0, 6.0], 'C': ['bar', 'foobarbaz'], 'D': [pd.Timestamp('2013-01-01'), pd.NaT]}, index=['min', 'sum'])
    with tm.assert_produces_warning(None):
        result = mdf.agg(['min', 'sum'])
    tm.assert_frame_equal(result, expected)
    with tm.assert_produces_warning(None):
        result = mdf[['D', 'C', 'B', 'A']].agg(['sum', 'min'])
    expected = expected[['D', 'C', 'B', 'A']]
    tm.assert_frame_equal(result, expected)