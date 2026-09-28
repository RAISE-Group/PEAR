def test_cat_accessor_updates_on_inplace(self):
    s = Series(list('abc')).astype('category')
    s.drop(0, inplace=True)
    s.cat.remove_unused_categories(inplace=True)
    assert len(s.cat.categories) == 2