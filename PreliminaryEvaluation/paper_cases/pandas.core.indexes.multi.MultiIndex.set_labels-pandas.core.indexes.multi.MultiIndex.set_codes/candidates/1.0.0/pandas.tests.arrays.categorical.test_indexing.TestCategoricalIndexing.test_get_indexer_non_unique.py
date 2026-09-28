@pytest.mark.parametrize('idx_values', [[1, 2, 3, 4], [1, 3, 2, 4], [1, 3, 3, 4], [1, 2, 2, 4]])
@pytest.mark.parametrize('key_values', [[1, 2], [1, 5], [1, 1], [5, 5]])
@pytest.mark.parametrize('key_class', [Categorical, CategoricalIndex])
def test_get_indexer_non_unique(self, idx_values, key_values, key_class):
    key = key_class(key_values, categories=range(1, 5))
    for dtype in (None, 'category', key.dtype):
        idx = Index(idx_values, dtype=dtype)
        expected, exp_miss = idx.get_indexer_non_unique(key_values)
        result, res_miss = idx.get_indexer_non_unique(key)
        tm.assert_numpy_array_equal(expected, result)
        tm.assert_numpy_array_equal(exp_miss, res_miss)