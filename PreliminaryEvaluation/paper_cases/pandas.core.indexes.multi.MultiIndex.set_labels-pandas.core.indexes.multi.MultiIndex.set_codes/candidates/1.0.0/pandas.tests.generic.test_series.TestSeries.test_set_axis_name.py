def test_set_axis_name(self):
    s = Series([1, 2, 3], index=['a', 'b', 'c'])
    funcs = ['rename_axis', '_set_axis_name']
    name = 'foo'
    for func in funcs:
        result = methodcaller(func, name)(s)
        assert s.index.name is None
        assert result.index.name == name