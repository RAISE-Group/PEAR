def test_loc_getitem_list_with_fail(self):
    s = Series([1, 2, 3])
    s.loc[[2]]
    with pytest.raises(KeyError, match=re.escape('"None of [Int64Index([3], dtype=\'int64\')] are in the [index]"')):
        s.loc[[3]]
    with pytest.raises(KeyError, match='with any missing labels'):
        s.loc[[2, 3]]