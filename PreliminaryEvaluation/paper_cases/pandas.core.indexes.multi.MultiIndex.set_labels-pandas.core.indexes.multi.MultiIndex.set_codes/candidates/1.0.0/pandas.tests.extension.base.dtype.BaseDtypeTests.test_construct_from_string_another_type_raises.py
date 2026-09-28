def test_construct_from_string_another_type_raises(self, dtype):
    msg = f"Cannot construct a '{type(dtype).__name__}' from 'another_type'"
    with pytest.raises(TypeError, match=msg):
        type(dtype).construct_from_string('another_type')