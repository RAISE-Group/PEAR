def test_logical_operators_int_dtype_with_str(self):
    s_1111 = Series([1] * 4, dtype='int8')
    with pytest.raises(TypeError):
        s_1111 & 'a'
    with pytest.raises(TypeError):
        s_1111 & ['a', 'b', 'c', 'd']