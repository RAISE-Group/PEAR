def test_set_name_methods(self, indices):
    new_name = 'This is the new name for this index'
    if isinstance(indices, MultiIndex):
        pytest.skip('Skip check for MultiIndex')
    original_name = indices.name
    new_ind = indices.set_names([new_name])
    assert new_ind.name == new_name
    assert indices.name == original_name
    res = indices.rename(new_name, inplace=True)
    assert res is None
    assert indices.name == new_name
    assert indices.names == [new_name]
    with pytest.raises(ValueError, match='Level must be None'):
        indices.set_names('a', level=0)
    name = ('A', 'B')
    indices.rename(name, inplace=True)
    assert indices.name == name
    assert indices.names == [name]