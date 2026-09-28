def test_mul_index(self, numeric_idx):
    idx = numeric_idx
    if not isinstance(idx, pd.RangeIndex):
        result = idx * idx
        tm.assert_index_equal(result, idx ** 2)