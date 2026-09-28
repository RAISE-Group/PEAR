def test_corrwith_with_objects(self):
    df1 = tm.makeTimeDataFrame()
    df2 = tm.makeTimeDataFrame()
    cols = ['A', 'B', 'C', 'D']
    df1['obj'] = 'foo'
    df2['obj'] = 'bar'
    result = df1.corrwith(df2)
    expected = df1.loc[:, cols].corrwith(df2.loc[:, cols])
    tm.assert_series_equal(result, expected)
    result = df1.corrwith(df2, axis=1)
    expected = df1.loc[:, cols].corrwith(df2.loc[:, cols], axis=1)
    tm.assert_series_equal(result, expected)