def test_logical_operators_int_dtype_with_float(self):
    s_0123 = Series(range(4), dtype='int64')
    with pytest.raises(TypeError):
        s_0123 & np.NaN
    with pytest.raises(TypeError):
        s_0123 & 3.14
    with pytest.raises(TypeError):
        s_0123 & [0.1, 4, 3.14, 2]
    with pytest.raises(TypeError):
        s_0123 & np.array([0.1, 4, 3.14, 2])
    with pytest.raises(TypeError):
        s_0123 & Series([0.1, 4, -3.14, 2])