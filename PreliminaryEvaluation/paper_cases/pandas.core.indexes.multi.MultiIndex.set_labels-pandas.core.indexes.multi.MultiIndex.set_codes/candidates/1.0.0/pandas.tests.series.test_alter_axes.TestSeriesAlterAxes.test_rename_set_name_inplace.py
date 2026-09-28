def test_rename_set_name_inplace(self):
    s = Series(range(3), index=list('abc'))
    for name in ['foo', 123, 123.0, datetime(2001, 11, 11), ('foo',)]:
        s.rename(name, inplace=True)
        assert s.name == name
        exp = np.array(['a', 'b', 'c'], dtype=np.object_)
        tm.assert_numpy_array_equal(s.index.values, exp)