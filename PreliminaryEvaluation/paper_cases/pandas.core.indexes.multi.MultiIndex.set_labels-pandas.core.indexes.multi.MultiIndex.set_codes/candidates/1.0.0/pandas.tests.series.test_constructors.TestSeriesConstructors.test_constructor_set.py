def test_constructor_set(self):
    values = {1, 2, 3, 4, 5}
    with pytest.raises(TypeError, match="'set' type is unordered"):
        Series(values)
    values = frozenset(values)
    with pytest.raises(TypeError, match="'frozenset' type is unordered"):
        Series(values)