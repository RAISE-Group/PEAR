def test_cat_accessor_api(self):
    from pandas.core.arrays.categorical import CategoricalAccessor
    assert Series.cat is CategoricalAccessor
    s = Series(list('aabbcde')).astype('category')
    assert isinstance(s.cat, CategoricalAccessor)
    invalid = Series([1])
    with pytest.raises(AttributeError, match='only use .cat accessor'):
        invalid.cat
    assert not hasattr(invalid, 'cat')