@pytest.mark.parametrize('mapper', [Series(['foo', 2.0, 'baz'], index=[0, 2, -1]), {0: 'foo', 2: 2.0, -1: 'baz'}])
def test_map_with_non_function_missing_values(self, mapper):
    expected = Index([2.0, np.nan, 'foo'])
    result = Index([2, 1, 0]).map(mapper)
    tm.assert_index_equal(expected, result)