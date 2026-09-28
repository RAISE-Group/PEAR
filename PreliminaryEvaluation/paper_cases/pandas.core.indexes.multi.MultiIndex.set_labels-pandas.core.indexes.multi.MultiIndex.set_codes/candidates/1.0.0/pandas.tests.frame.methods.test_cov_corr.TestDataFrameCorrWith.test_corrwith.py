def test_corrwith(self, datetime_frame):
    a = datetime_frame
    noise = Series(np.random.randn(len(a)), index=a.index)
    b = datetime_frame.add(noise, axis=0)
    b = b.reindex(columns=b.columns[::-1], index=b.index[::-1][10:])
    del b['B']
    colcorr = a.corrwith(b, axis=0)
    tm.assert_almost_equal(colcorr['A'], a['A'].corr(b['A']))
    rowcorr = a.corrwith(b, axis=1)
    tm.assert_series_equal(rowcorr, a.T.corrwith(b.T, axis=0))
    dropped = a.corrwith(b, axis=0, drop=True)
    tm.assert_almost_equal(dropped['A'], a['A'].corr(b['A']))
    assert 'B' not in dropped
    dropped = a.corrwith(b, axis=1, drop=True)
    assert a.index[-1] not in dropped.index
    index = ['a', 'b', 'c', 'd', 'e']
    columns = ['one', 'two', 'three', 'four']
    df1 = DataFrame(np.random.randn(5, 4), index=index, columns=columns)
    df2 = DataFrame(np.random.randn(4, 4), index=index[:4], columns=columns)
    correls = df1.corrwith(df2, axis=1)
    for row in index[:4]:
        tm.assert_almost_equal(correls[row], df1.loc[row].corr(df2.loc[row]))