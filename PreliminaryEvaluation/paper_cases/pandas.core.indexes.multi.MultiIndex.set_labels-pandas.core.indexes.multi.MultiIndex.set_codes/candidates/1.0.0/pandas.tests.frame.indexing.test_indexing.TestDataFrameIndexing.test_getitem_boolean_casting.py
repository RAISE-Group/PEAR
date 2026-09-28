def test_getitem_boolean_casting(self, datetime_frame):
    df = datetime_frame.copy()
    df['E'] = 1
    df['E'] = df['E'].astype('int32')
    df['E1'] = df['E'].copy()
    df['F'] = 1
    df['F'] = df['F'].astype('int64')
    df['F1'] = df['F'].copy()
    casted = df[df > 0]
    result = casted.dtypes
    expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] * 2 + [np.dtype('int64')] * 2, index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
    tm.assert_series_equal(result, expected)
    df.loc[df.index[1:3], ['E1', 'F1']] = 0
    casted = df[df > 0]
    result = casted.dtypes
    expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] + [np.dtype('float64')] + [np.dtype('int64')] + [np.dtype('float64')], index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
    tm.assert_series_equal(result, expected)
    df = DataFrame(data=np.random.randn(100, 50))
    df = df.where(df > 0)
    bools = df > 0
    mask = isna(df)
    expected = bools.astype(float).mask(mask)
    result = bools.mask(mask)
    tm.assert_frame_equal(result, expected)