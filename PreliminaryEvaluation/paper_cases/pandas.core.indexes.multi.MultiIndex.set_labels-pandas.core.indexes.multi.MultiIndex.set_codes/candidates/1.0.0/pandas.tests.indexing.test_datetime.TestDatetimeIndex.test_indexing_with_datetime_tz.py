def test_indexing_with_datetime_tz(self):
    idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
    dr = date_range('20130110', periods=3)
    df = DataFrame({'A': idx, 'B': dr})
    df['C'] = idx
    df.iloc[1, 1] = pd.NaT
    df.iloc[1, 2] = pd.NaT
    result = df.iloc[1]
    expected = Series([Timestamp('2013-01-02 00:00:00-0500', tz='US/Eastern'), pd.NaT, pd.NaT], index=list('ABC'), dtype='object', name=1)
    tm.assert_series_equal(result, expected)
    result = df.loc[1]
    expected = Series([Timestamp('2013-01-02 00:00:00-0500', tz='US/Eastern'), pd.NaT, pd.NaT], index=list('ABC'), dtype='object', name=1)
    tm.assert_series_equal(result, expected)
    df = DataFrame({'a': date_range('2014-01-01', periods=10, tz='UTC')})
    result = df.iloc[5]
    expected = Series([Timestamp('2014-01-06 00:00:00+0000', tz='UTC')], index=['a'], name=5)
    tm.assert_series_equal(result, expected)
    result = df.loc[5]
    tm.assert_series_equal(result, expected)
    result = df[df.a > df.a[3]]
    expected = df.iloc[4:]
    tm.assert_frame_equal(result, expected)
    df = DataFrame(data=pd.to_datetime(['2015-03-30 20:12:32', '2015-03-12 00:11:11']), columns=['time'])
    df['new_col'] = ['new', 'old']
    df.time = df.set_index('time').index.tz_localize('UTC')
    v = df[df.new_col == 'new'].set_index('time').index.tz_convert('US/Pacific')
    df2 = df.copy()
    df2.loc[df2.new_col == 'new', 'time'] = v
    expected = Series([v[0], df.loc[1, 'time']], name='time')
    tm.assert_series_equal(df2.time, expected)
    v = df.loc[df.new_col == 'new', 'time'] + pd.Timedelta('1s')
    df.loc[df.new_col == 'new', 'time'] = v
    tm.assert_series_equal(df.loc[df.new_col == 'new', 'time'], v)