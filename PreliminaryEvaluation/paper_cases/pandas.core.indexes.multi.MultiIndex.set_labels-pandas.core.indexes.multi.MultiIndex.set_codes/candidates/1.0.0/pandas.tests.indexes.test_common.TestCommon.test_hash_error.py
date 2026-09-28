def test_hash_error(self, indices):
    index = indices
    with pytest.raises(TypeError, match=f"unhashable type: '{type(index).__name__}'"):
        hash(indices)