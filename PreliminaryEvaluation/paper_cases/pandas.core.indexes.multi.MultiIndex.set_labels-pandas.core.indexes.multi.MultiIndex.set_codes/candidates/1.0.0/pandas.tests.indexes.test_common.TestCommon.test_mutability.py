def test_mutability(self, indices):
    if not len(indices):
        pytest.skip('Skip check for empty Index')
    msg = 'Index does not support mutable operations'
    with pytest.raises(TypeError, match=msg):
        indices[0] = indices[0]