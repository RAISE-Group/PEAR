def test_setitem_chained_setfault(self):
    data = ['right', 'left', 'left', 'left', 'right', 'left', 'timeout']
    mdata = ['right', 'left', 'left', 'left', 'right', 'left', 'none']
    df = DataFrame({'response': np.array(data)})
    mask = df.response == 'timeout'
    df.response[mask] = 'none'
    tm.assert_frame_equal(df, DataFrame({'response': mdata}))
    recarray = np.rec.fromarrays([data], names=['response'])
    df = DataFrame(recarray)
    mask = df.response == 'timeout'
    df.response[mask] = 'none'
    tm.assert_frame_equal(df, DataFrame({'response': mdata}))
    df = DataFrame({'response': data, 'response1': data})
    mask = df.response == 'timeout'
    df.response[mask] = 'none'
    tm.assert_frame_equal(df, DataFrame({'response': mdata, 'response1': data}))
    expected = DataFrame(dict(A=[np.nan, 'bar', 'bah', 'foo', 'bar']))
    df = DataFrame(dict(A=np.array(['foo', 'bar', 'bah', 'foo', 'bar'])))
    df['A'].iloc[0] = np.nan
    result = df.head()
    tm.assert_frame_equal(result, expected)
    df = DataFrame(dict(A=np.array(['foo', 'bar', 'bah', 'foo', 'bar'])))
    df.A.iloc[0] = np.nan
    result = df.head()
    tm.assert_frame_equal(result, expected)