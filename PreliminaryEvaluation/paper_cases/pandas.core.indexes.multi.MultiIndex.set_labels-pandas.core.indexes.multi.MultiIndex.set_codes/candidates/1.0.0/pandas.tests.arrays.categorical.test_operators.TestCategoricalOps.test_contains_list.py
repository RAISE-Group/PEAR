def test_contains_list(self):
    cat = Categorical([1, 2, 3])
    assert 'a' not in cat
    with pytest.raises(TypeError, match='unhashable type'):
        ['a'] in cat
    with pytest.raises(TypeError, match='unhashable type'):
        ['a', 'b'] in cat