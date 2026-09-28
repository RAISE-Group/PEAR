@pytest.mark.parametrize('dtype', [SparseDtype(int, 0), int])
def test_constructor_na_dtype(self, dtype):
    with pytest.raises(ValueError, match='Cannot convert'):
        SparseArray([0, 1, np.nan], dtype=dtype)