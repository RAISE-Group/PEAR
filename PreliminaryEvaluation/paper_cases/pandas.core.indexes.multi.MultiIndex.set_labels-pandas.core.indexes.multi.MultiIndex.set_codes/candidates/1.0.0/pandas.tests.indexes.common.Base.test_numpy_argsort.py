def test_numpy_argsort(self, indices):
    result = np.argsort(indices)
    expected = indices.argsort()
    tm.assert_numpy_array_equal(result, expected)
    if isinstance(type(indices), (CategoricalIndex, RangeIndex)):
        msg = "the 'axis' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            np.argsort(indices, axis=1)
        msg = "the 'kind' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            np.argsort(indices, kind='mergesort')
        msg = "the 'order' parameter is not supported"
        with pytest.raises(ValueError, match=msg):
            np.argsort(indices, order=('a', 'b'))