def test_center_ljust_rjust_fillchar(self):
    values = Series(['a', 'bb', 'cccc', 'ddddd', 'eeeeee'])
    result = values.str.center(5, fillchar='X')
    expected = Series(['XXaXX', 'XXbbX', 'Xcccc', 'ddddd', 'eeeeee'])
    tm.assert_series_equal(result, expected)
    expected = np.array([v.center(5, 'X') for v in values.values], dtype=np.object_)
    tm.assert_numpy_array_equal(result.values, expected)
    result = values.str.ljust(5, fillchar='X')
    expected = Series(['aXXXX', 'bbXXX', 'ccccX', 'ddddd', 'eeeeee'])
    tm.assert_series_equal(result, expected)
    expected = np.array([v.ljust(5, 'X') for v in values.values], dtype=np.object_)
    tm.assert_numpy_array_equal(result.values, expected)
    result = values.str.rjust(5, fillchar='X')
    expected = Series(['XXXXa', 'XXXbb', 'Xcccc', 'ddddd', 'eeeeee'])
    tm.assert_series_equal(result, expected)
    expected = np.array([v.rjust(5, 'X') for v in values.values], dtype=np.object_)
    tm.assert_numpy_array_equal(result.values, expected)
    template = 'fillchar must be a character, not {dtype}'
    with pytest.raises(TypeError, match=template.format(dtype='str')):
        values.str.center(5, fillchar='XY')
    with pytest.raises(TypeError, match=template.format(dtype='str')):
        values.str.ljust(5, fillchar='XY')
    with pytest.raises(TypeError, match=template.format(dtype='str')):
        values.str.rjust(5, fillchar='XY')
    with pytest.raises(TypeError, match=template.format(dtype='int')):
        values.str.center(5, fillchar=1)
    with pytest.raises(TypeError, match=template.format(dtype='int')):
        values.str.ljust(5, fillchar=1)
    with pytest.raises(TypeError, match=template.format(dtype='int')):
        values.str.rjust(5, fillchar=1)