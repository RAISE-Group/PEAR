def test_str_accessor_no_new_attributes(self):
    s = Series(list('aabbcde'))
    with pytest.raises(AttributeError, match='You cannot add any new attribute'):
        s.str.xlabel = 'a'