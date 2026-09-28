def test_loc_setitem_consistency(self):
    expected = DataFrame({'date': Series(0, index=range(5), dtype=np.int64), 'val': Series(range(5), dtype=np.int64)})
    df = DataFrame({'date': date_range('2000-01-01', '2000-01-5'), 'val': Series(range(5), dtype=np.int64)})
    df.loc[:, 'date'] = 0
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'date': date_range('2000-01-01', '2000-01-5'), 'val': Series(range(5), dtype=np.int64)})
    df.loc[:, 'date'] = np.array(0, dtype=np.int64)
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'date': date_range('2000-01-01', '2000-01-5'), 'val': Series(range(5), dtype=np.int64)})
    df.loc[:, 'date'] = np.array([0, 0, 0, 0, 0], dtype=np.int64)
    tm.assert_frame_equal(df, expected)
    expected = DataFrame({'date': Series('foo', index=range(5)), 'val': Series(range(5), dtype=np.int64)})
    df = DataFrame({'date': date_range('2000-01-01', '2000-01-5'), 'val': Series(range(5), dtype=np.int64)})
    df.loc[:, 'date'] = 'foo'
    tm.assert_frame_equal(df, expected)
    expected = DataFrame({'date': Series(1.0, index=range(5)), 'val': Series(range(5), dtype=np.int64)})
    df = DataFrame({'date': date_range('2000-01-01', '2000-01-5'), 'val': Series(range(5), dtype=np.int64)})
    df.loc[:, 'date'] = 1.0
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'date': Series([Timestamp('20180101')])})
    df.loc[:, 'date'] = 'string'
    expected = DataFrame({'date': Series(['string'])})
    tm.assert_frame_equal(df, expected)