def test_not_hashable(self):
    empty_frame = DataFrame()
    df = DataFrame([1])
    msg = "'DataFrame' objects are mutable, thus they cannot be hashed"
    with pytest.raises(TypeError, match=msg):
        hash(df)
    with pytest.raises(TypeError, match=msg):
        hash(empty_frame)