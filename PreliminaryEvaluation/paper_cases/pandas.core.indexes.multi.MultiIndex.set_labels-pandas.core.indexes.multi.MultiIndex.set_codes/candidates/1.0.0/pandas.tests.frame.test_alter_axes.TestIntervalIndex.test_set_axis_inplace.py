def test_set_axis_inplace(self):
    df = DataFrame({'A': [1.1, 2.2, 3.3], 'B': [5.0, 6.1, 7.2], 'C': [4.4, 5.5, 6.6]}, index=[2010, 2011, 2012])
    expected = {0: df.copy(), 1: df.copy()}
    expected[0].index = list('abc')
    expected[1].columns = list('abc')
    expected['index'] = expected[0]
    expected['columns'] = expected[1]
    for axis in expected:
        result = df.copy()
        result.set_axis(list('abc'), axis=axis, inplace=True)
        tm.assert_frame_equal(result, expected[axis])
        result = df.set_axis(list('abc'), axis=axis)
        tm.assert_frame_equal(expected[axis], result)
    with tm.assert_produces_warning(None):
        result = df.set_axis(list('abc'))
    tm.assert_frame_equal(result, expected[0])
    for axis in (3, 'foo'):
        with pytest.raises(ValueError, match='No axis named'):
            df.set_axis(list('abc'), axis=axis)