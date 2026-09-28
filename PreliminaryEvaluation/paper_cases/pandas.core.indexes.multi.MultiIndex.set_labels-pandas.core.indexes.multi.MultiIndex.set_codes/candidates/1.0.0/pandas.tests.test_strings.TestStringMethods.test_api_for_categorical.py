def test_api_for_categorical(self, any_string_method):
    s = Series(list('aabb'))
    s = s + ' ' + s
    c = s.astype('category')
    assert isinstance(c.str, strings.StringMethods)
    method_name, args, kwargs = any_string_method
    result = getattr(c.str, method_name)(*args, **kwargs)
    expected = getattr(s.str, method_name)(*args, **kwargs)
    if isinstance(result, DataFrame):
        tm.assert_frame_equal(result, expected)
    elif isinstance(result, Series):
        tm.assert_series_equal(result, expected)
    else:
        assert result == expected