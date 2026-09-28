def test_contains_list(self):
    idx = pd.CategoricalIndex([1, 2, 3])
    assert 'a' not in idx
    with pytest.raises(TypeError, match='unhashable type'):
        ['a'] in idx
    with pytest.raises(TypeError, match='unhashable type'):
        ['a', 'b'] in idx