def test_set_axis_name(self):
    df = pd.DataFrame([[1, 2], [3, 4]])
    funcs = ['_set_axis_name', 'rename_axis']
    for func in funcs:
        result = methodcaller(func, 'foo')(df)
        assert df.index.name is None
        assert result.index.name == 'foo'
        result = methodcaller(func, 'cols', axis=1)(df)
        assert df.columns.name is None
        assert result.columns.name == 'cols'