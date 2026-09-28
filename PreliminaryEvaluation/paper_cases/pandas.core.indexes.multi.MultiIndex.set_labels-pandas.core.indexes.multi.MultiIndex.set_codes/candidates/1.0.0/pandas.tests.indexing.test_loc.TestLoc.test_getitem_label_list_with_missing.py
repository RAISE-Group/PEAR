def test_getitem_label_list_with_missing(self):
    s = Series(range(3), index=['a', 'b', 'c'])
    with pytest.raises(KeyError, match='with any missing labels'):
        s[['a', 'd']]
    s = Series(range(3))
    with pytest.raises(KeyError, match='with any missing labels'):
        s[[0, 3]]