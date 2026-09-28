def test_constructor_corner(self):
    arr = np.array([1, 2, 3, 4], dtype=object)
    index = RangeIndex(1, 5)
    assert index.values.dtype == np.int64
    tm.assert_index_equal(index, Index(arr))
    with pytest.raises(TypeError):
        RangeIndex('1', '10', '1')
    with pytest.raises(TypeError):
        RangeIndex(1.1, 10.2, 1.3)
    with pytest.raises(ValueError, match='Incorrect `dtype` passed: expected signed integer, received float64'):
        RangeIndex(1, 5, dtype='float64')