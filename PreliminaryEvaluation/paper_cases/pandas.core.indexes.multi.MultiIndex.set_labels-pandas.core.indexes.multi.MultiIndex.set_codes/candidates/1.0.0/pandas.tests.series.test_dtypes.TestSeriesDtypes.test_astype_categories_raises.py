def test_astype_categories_raises(self):
    s = Series(['a', 'b', 'a'])
    with pytest.raises(TypeError, match='got an unexpected'):
        s.astype('category', categories=['a', 'b'], ordered=True)