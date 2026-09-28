def test_cat_accessor_no_new_attributes(self):
    c = Series(list('aabbcde')).astype('category')
    with pytest.raises(AttributeError, match='You cannot add any new attribute'):
        c.cat.xlabel = 'a'