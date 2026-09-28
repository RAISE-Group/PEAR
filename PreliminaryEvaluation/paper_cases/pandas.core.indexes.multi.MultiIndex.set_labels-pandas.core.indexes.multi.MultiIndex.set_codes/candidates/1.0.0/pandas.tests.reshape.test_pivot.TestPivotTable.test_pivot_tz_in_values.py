def test_pivot_tz_in_values(self):
    df = pd.DataFrame([{'uid': 'aa', 'ts': pd.Timestamp('2016-08-12 13:00:00-0700', tz='US/Pacific')}, {'uid': 'aa', 'ts': pd.Timestamp('2016-08-12 08:00:00-0700', tz='US/Pacific')}, {'uid': 'aa', 'ts': pd.Timestamp('2016-08-12 14:00:00-0700', tz='US/Pacific')}, {'uid': 'aa', 'ts': pd.Timestamp('2016-08-25 11:00:00-0700', tz='US/Pacific')}, {'uid': 'aa', 'ts': pd.Timestamp('2016-08-25 13:00:00-0700', tz='US/Pacific')}])
    df = df.set_index('ts').reset_index()
    mins = df.ts.map(lambda x: x.replace(hour=0, minute=0, second=0, microsecond=0))
    result = pd.pivot_table(df.set_index('ts').reset_index(), values='ts', index=['uid'], columns=[mins], aggfunc=np.min)
    expected = pd.DataFrame([[pd.Timestamp('2016-08-12 08:00:00-0700', tz='US/Pacific'), pd.Timestamp('2016-08-25 11:00:00-0700', tz='US/Pacific')]], index=pd.Index(['aa'], name='uid'), columns=pd.DatetimeIndex([pd.Timestamp('2016-08-12 00:00:00', tz='US/Pacific'), pd.Timestamp('2016-08-25 00:00:00', tz='US/Pacific')], name='ts'))
    tm.assert_frame_equal(result, expected)