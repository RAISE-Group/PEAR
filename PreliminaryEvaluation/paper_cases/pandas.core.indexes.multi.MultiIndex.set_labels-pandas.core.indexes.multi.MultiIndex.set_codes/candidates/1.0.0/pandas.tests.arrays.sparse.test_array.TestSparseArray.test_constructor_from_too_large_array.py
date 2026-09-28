def test_constructor_from_too_large_array(self):
    with pytest.raises(TypeError, match='expected dimension <= 1 data'):
        SparseArray(np.arange(10).reshape((2, 5)))