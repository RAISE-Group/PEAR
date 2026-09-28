def test_set_axis_name_mi(self):
    df = DataFrame(np.empty((3, 3)), index=MultiIndex.from_tuples([('A', x) for x in list('aBc')]), columns=MultiIndex.from_tuples([('C', x) for x in list('xyz')]))
    level_names = ['L1', 'L2']
    funcs = ['_set_axis_name', 'rename_axis']
    for func in funcs:
        result = methodcaller(func, level_names)(df)
        assert result.index.names == level_names
        assert result.columns.names == [None, None]
        result = methodcaller(func, level_names, axis=1)(df)
        assert result.columns.names == ['L1', 'L2']
        assert result.index.names == [None, None]