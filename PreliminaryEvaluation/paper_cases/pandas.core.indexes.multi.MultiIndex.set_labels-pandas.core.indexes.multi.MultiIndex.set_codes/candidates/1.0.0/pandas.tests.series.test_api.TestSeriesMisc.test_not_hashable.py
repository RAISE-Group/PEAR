def test_not_hashable(self):
    s_empty = Series(dtype=object)
    s = Series([1])
    msg = "'Series' objects are mutable, thus they cannot be hashed"
    with pytest.raises(TypeError, match=msg):
        hash(s_empty)
    with pytest.raises(TypeError, match=msg):
        hash(s)