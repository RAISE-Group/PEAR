def test_constructor_str_unknown(self):
    with pytest.raises(ValueError, match='Unknown dtype'):
        Categorical([1, 2], dtype='foo')