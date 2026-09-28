def test_join_append_timedeltas(self):
    d = {'d': datetime(2013, 11, 5, 5, 56), 't': timedelta(0, 22500)}
    df = DataFrame(columns=list('dt'))
    df = df.append(d, ignore_index=True)
    result = df.append(d, ignore_index=True)
    expected = DataFrame({'d': [datetime(2013, 11, 5, 5, 56), datetime(2013, 11, 5, 5, 56)], 't': [timedelta(0, 22500), timedelta(0, 22500)]})
    tm.assert_frame_equal(result, expected)
    td = np.timedelta64(300000000)
    lhs = DataFrame(Series([td, td], index=['A', 'B']))
    rhs = DataFrame(Series([td], index=['A']))
    result = lhs.join(rhs, rsuffix='r', how='left')
    expected = DataFrame({'0': Series([td, td], index=list('AB')), '0r': Series([td, pd.NaT], index=list('AB'))})
    tm.assert_frame_equal(result, expected)