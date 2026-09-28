def test_invalid_raises(self):
    with pytest.raises(TypeError, match='ordered'):
        CategoricalDtype(['a', 'b'], ordered='foo')
    with pytest.raises(TypeError, match="'categories' must be list-like"):
        CategoricalDtype('category')