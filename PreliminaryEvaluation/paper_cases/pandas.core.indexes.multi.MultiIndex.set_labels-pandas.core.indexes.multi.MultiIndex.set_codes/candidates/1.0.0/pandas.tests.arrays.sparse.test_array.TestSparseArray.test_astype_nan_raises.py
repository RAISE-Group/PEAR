def test_astype_nan_raises(self):
    arr = SparseArray([1.0, np.nan])
    with pytest.raises(ValueError, match='Cannot convert non-finite'):
        arr.astype(int)