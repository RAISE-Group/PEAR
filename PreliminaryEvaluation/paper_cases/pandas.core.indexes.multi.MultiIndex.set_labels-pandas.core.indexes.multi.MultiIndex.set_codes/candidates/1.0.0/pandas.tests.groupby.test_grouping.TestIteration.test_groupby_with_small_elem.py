def test_groupby_with_small_elem(self):
    df = pd.DataFrame({'event': ['start', 'start'], 'change': [1234, 5678]}, index=pd.DatetimeIndex(['2014-09-10', '2013-10-10']))
    grouped = df.groupby([pd.Grouper(freq='M'), 'event'])
    assert len(grouped.groups) == 2
    assert grouped.ngroups == 2
    assert (pd.Timestamp('2014-09-30'), 'start') in grouped.groups
    assert (pd.Timestamp('2013-10-31'), 'start') in grouped.groups
    res = grouped.get_group((pd.Timestamp('2014-09-30'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[0], :])
    res = grouped.get_group((pd.Timestamp('2013-10-31'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[1], :])
    df = pd.DataFrame({'event': ['start', 'start', 'start'], 'change': [1234, 5678, 9123]}, index=pd.DatetimeIndex(['2014-09-10', '2013-10-10', '2014-09-15']))
    grouped = df.groupby([pd.Grouper(freq='M'), 'event'])
    assert len(grouped.groups) == 2
    assert grouped.ngroups == 2
    assert (pd.Timestamp('2014-09-30'), 'start') in grouped.groups
    assert (pd.Timestamp('2013-10-31'), 'start') in grouped.groups
    res = grouped.get_group((pd.Timestamp('2014-09-30'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[0, 2], :])
    res = grouped.get_group((pd.Timestamp('2013-10-31'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[1], :])
    df = pd.DataFrame({'event': ['start', 'start', 'start'], 'change': [1234, 5678, 9123]}, index=pd.DatetimeIndex(['2014-09-10', '2013-10-10', '2014-08-05']))
    grouped = df.groupby([pd.Grouper(freq='M'), 'event'])
    assert len(grouped.groups) == 3
    assert grouped.ngroups == 3
    assert (pd.Timestamp('2014-09-30'), 'start') in grouped.groups
    assert (pd.Timestamp('2013-10-31'), 'start') in grouped.groups
    assert (pd.Timestamp('2014-08-31'), 'start') in grouped.groups
    res = grouped.get_group((pd.Timestamp('2014-09-30'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[0], :])
    res = grouped.get_group((pd.Timestamp('2013-10-31'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[1], :])
    res = grouped.get_group((pd.Timestamp('2014-08-31'), 'start'))
    tm.assert_frame_equal(res, df.iloc[[2], :])