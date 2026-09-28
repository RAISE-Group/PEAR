def test_set_axis_name_mi(self):
    s = Series([11, 21, 31], index=MultiIndex.from_tuples([('A', x) for x in ['a', 'B', 'c']], names=['l1', 'l2']))
    funcs = ['rename_axis', '_set_axis_name']
    for func in funcs:
        result = methodcaller(func, ['L1', 'L2'])(s)
        assert s.index.name is None
        assert s.index.names == ['l1', 'l2']
        assert result.index.name is None
        assert result.index.names, ['L1', 'L2']