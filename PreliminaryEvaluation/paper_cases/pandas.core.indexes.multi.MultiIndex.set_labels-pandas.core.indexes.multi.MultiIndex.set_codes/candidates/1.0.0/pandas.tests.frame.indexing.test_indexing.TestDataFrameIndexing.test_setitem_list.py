def test_setitem_list(self, float_frame):
    float_frame['E'] = 'foo'
    data = float_frame[['A', 'B']]
    float_frame[['B', 'A']] = data
    tm.assert_series_equal(float_frame['B'], data['A'], check_names=False)
    tm.assert_series_equal(float_frame['A'], data['B'], check_names=False)
    msg = 'Columns must be same length as key'
    with pytest.raises(ValueError, match=msg):
        data[['A']] = float_frame[['A', 'B']]
    msg = 'Length of values does not match length of index'
    with pytest.raises(ValueError, match=msg):
        data['A'] = range(len(data.index) - 1)
    df = DataFrame(0, index=range(3), columns=['tt1', 'tt2'], dtype=np.int_)
    df.loc[1, ['tt1', 'tt2']] = [1, 2]
    result = df.loc[df.index[1], ['tt1', 'tt2']]
    expected = Series([1, 2], df.columns, dtype=np.int_, name=1)
    tm.assert_series_equal(result, expected)
    df['tt1'] = df['tt2'] = '0'
    df.loc[df.index[1], ['tt1', 'tt2']] = ['1', '2']
    result = df.loc[df.index[1], ['tt1', 'tt2']]
    expected = Series(['1', '2'], df.columns, name=1)
    tm.assert_series_equal(result, expected)