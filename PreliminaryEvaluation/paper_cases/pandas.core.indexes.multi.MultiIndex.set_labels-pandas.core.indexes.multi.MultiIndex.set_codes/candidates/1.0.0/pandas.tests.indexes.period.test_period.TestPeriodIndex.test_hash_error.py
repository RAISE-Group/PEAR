def test_hash_error(self):
    index = period_range('20010101', periods=10)
    msg = f"unhashable type: '{type(index).__name__}'"
    with pytest.raises(TypeError, match=msg):
        hash(index)