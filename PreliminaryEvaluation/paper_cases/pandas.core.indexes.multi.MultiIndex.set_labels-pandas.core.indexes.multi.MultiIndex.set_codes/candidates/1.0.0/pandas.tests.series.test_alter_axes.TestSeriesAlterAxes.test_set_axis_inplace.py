def test_set_axis_inplace(self):
    s = Series(np.arange(4), index=[1, 3, 5, 7], dtype='int64')
    expected = s.copy()
    expected.index = list('abcd')
    result = s.set_axis(list('abcd'), axis=0, inplace=False)
    tm.assert_series_equal(expected, result)
    with tm.assert_produces_warning(None):
        result = s.set_axis(list('abcd'), inplace=False)
    tm.assert_series_equal(result, expected)
    for axis in [2, 'foo']:
        with pytest.raises(ValueError, match='No axis named'):
            s.set_axis(list('abcd'), axis=axis, inplace=False)