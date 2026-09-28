def test_delete_base(self, indices):
    if not len(indices):
        return
    if isinstance(indices, RangeIndex):
        return
    expected = indices[1:]
    result = indices.delete(0)
    assert result.equals(expected)
    assert result.name == expected.name
    expected = indices[:-1]
    result = indices.delete(-1)
    assert result.equals(expected)
    assert result.name == expected.name
    with pytest.raises((IndexError, ValueError)):
        indices.delete(len(indices))