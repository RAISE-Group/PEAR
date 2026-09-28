def test_rename_set_name(self):
    s = Series(range(4), index=list('abcd'))
    for name in ['foo', 123, 123.0, datetime(2001, 11, 11), ('foo',)]:
        result = s.rename(name)
        assert result.name == name
        tm.assert_numpy_array_equal(result.index.values, s.index.values)
        assert s.name is None