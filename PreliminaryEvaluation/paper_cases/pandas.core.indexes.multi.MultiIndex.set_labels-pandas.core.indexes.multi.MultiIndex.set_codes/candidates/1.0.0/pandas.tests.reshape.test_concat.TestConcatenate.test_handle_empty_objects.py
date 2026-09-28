def test_handle_empty_objects(self, sort):
    df = DataFrame(np.random.randn(10, 4), columns=list('abcd'))
    baz = df[:5].copy()
    baz['foo'] = 'bar'
    empty = df[5:5]
    frames = [baz, empty, empty, df[5:]]
    concatted = concat(frames, axis=0, sort=sort)
    expected = df.reindex(columns=['a', 'b', 'c', 'd', 'foo'])
    expected['foo'] = expected['foo'].astype('O')
    expected.loc[0:4, 'foo'] = 'bar'
    tm.assert_frame_equal(concatted, expected)
    df = DataFrame(dict(A=range(10000)), index=date_range('20130101', periods=10000, freq='s'))
    empty = DataFrame()
    result = concat([df, empty], axis=1)
    tm.assert_frame_equal(result, df)
    result = concat([empty, df], axis=1)
    tm.assert_frame_equal(result, df)
    result = concat([df, empty])
    tm.assert_frame_equal(result, df)
    result = concat([empty, df])
    tm.assert_frame_equal(result, df)