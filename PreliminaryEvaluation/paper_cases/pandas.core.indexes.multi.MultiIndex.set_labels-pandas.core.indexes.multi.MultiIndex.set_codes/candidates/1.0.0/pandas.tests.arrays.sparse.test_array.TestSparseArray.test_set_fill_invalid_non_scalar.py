@pytest.mark.parametrize('val', [[1, 2, 3], np.array([1, 2]), (1, 2, 3)])
def test_set_fill_invalid_non_scalar(self, val):
    arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool)
    msg = 'fill_value must be a scalar'
    with pytest.raises(ValueError, match=msg):
        arr.fill_value = val