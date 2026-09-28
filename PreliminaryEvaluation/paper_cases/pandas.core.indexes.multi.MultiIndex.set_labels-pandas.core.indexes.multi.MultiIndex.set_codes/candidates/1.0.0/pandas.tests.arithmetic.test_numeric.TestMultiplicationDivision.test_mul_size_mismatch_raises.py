def test_mul_size_mismatch_raises(self, numeric_idx):
    idx = numeric_idx
    with pytest.raises(ValueError):
        idx * idx[0:3]
    with pytest.raises(ValueError):
        idx * np.array([1, 2])