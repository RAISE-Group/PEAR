def test_column_dups_indexing2(self):
    df = DataFrame({'A': np.arange(5, dtype='int64'), 'B': np.arange(1, 6, dtype='int64')}, index=[2, 2, 3, 3, 4])
    result = df.B - df.A
    expected = Series(1, index=[2, 2, 3, 3, 4])
    tm.assert_series_equal(result, expected)
    df = DataFrame({'A': date_range('20130101', periods=5), 'B': date_range('20130101 09:00:00', periods=5)}, index=[2, 2, 3, 3, 4])
    result = df.B - df.A
    expected = Series(pd.Timedelta('9 hours'), index=[2, 2, 3, 3, 4])
    tm.assert_series_equal(result, expected)