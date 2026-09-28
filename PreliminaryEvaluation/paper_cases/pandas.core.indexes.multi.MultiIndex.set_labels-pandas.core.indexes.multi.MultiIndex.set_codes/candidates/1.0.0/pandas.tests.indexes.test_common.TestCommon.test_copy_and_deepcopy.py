def test_copy_and_deepcopy(self, indices):
    from copy import copy, deepcopy
    if isinstance(indices, MultiIndex):
        pytest.skip('Skip check for MultiIndex')
    for func in (copy, deepcopy):
        idx_copy = func(indices)
        assert idx_copy is not indices
        assert idx_copy.equals(indices)
    new_copy = indices.copy(deep=True, name='banana')
    assert new_copy.name == 'banana'