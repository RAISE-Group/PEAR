def test_hash_error(self):
    index = date_range('20010101', periods=10)
    with pytest.raises(TypeError, match=f"unhashable type: '{type(index).__name__}'"):
        hash(index)