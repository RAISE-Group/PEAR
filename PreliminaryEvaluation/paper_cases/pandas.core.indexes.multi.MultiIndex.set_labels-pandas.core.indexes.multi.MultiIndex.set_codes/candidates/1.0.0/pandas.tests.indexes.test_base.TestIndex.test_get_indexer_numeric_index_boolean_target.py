@pytest.mark.parametrize('idx_class', [Int64Index, RangeIndex, Float64Index])
def test_get_indexer_numeric_index_boolean_target(self, idx_class):
    numeric_index = idx_class(RangeIndex(4))
    result = numeric_index.get_indexer([True, False, True])
    expected = np.array([-1, -1, -1], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)