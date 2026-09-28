def test_setitem_with_unaligned_tz_aware_datetime_column(self):
    column = pd.Series(pd.date_range('2015-01-01', periods=3, tz='utc'), name='dates')
    df = pd.DataFrame({'dates': column})
    df['dates'] = column[[1, 0, 2]]
    tm.assert_series_equal(df['dates'], column)
    df = pd.DataFrame({'dates': column})
    df.loc[[0, 1, 2], 'dates'] = column[[1, 0, 2]]
    tm.assert_series_equal(df['dates'], column)