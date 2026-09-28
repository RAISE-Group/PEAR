def test_constructor_invalid(self):
    msg = "Parameter 'categories' must be list-like"
    with pytest.raises(TypeError, match=msg):
        CategoricalDtype('category')