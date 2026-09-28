@pytest.mark.parametrize('arr, unique', [([(0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)]), ([('b', 'c'), ('a', 'b'), ('a', 'b'), ('b', 'c')], [('b', 'c'), ('a', 'b')]), ([('a', 1), ('b', 2), ('a', 3), ('a', 1)], [('a', 1), ('b', 2), ('a', 3)])])
def test_unique_tuples(self, arr, unique):
    expected = np.empty(len(unique), dtype=object)
    expected[:] = unique
    result = pd.unique(arr)
    tm.assert_numpy_array_equal(result, expected)