def test_constructor_corner(self):
    arr = np.array([1, 2, 3, 4], dtype=object)
    index = Int64Index(arr)
    assert index.values.dtype == np.int64
    tm.assert_index_equal(index, Index(arr))
    arr = np.array([1, '2', 3, '4'], dtype=object)
    with pytest.raises(TypeError, match='casting'):
        Int64Index(arr)
    arr_with_floats = [0, 2, 3, 4, 5, 1.25, 3, -1]
    with pytest.raises(TypeError, match='casting'):
        Int64Index(arr_with_floats)