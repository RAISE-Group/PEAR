def test_constructor_non_hashable_name(self, indices):
    if isinstance(indices, MultiIndex):
        pytest.skip('multiindex handled in test_multi.py')
    message = 'Index.name must be a hashable type'
    renamed = [['1']]
    with pytest.raises(TypeError, match=message):
        indices.rename(name=renamed)
    with pytest.raises(TypeError, match=message):
        indices.set_names(names=renamed)