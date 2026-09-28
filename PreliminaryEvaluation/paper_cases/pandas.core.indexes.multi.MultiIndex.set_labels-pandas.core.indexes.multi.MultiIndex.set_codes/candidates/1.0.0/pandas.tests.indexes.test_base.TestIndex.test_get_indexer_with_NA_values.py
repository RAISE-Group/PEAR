def test_get_indexer_with_NA_values(self, unique_nulls_fixture, unique_nulls_fixture2):
    if unique_nulls_fixture is unique_nulls_fixture2:
        return
    arr = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=np.object)
    index = pd.Index(arr, dtype=np.object)
    result = index.get_indexer([unique_nulls_fixture, unique_nulls_fixture2, 'Unknown'])
    expected = np.array([0, 1, -1], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)