@pytest.mark.parametrize('data, expected_codes, expected_uniques', [([(1, 1), (1, 2), (0, 0), (1, 2), 'nonsense'], [0, 1, 2, 1, 3], [(1, 1), (1, 2), (0, 0), 'nonsense']), ([(1, 1), (1, 2), (0, 0), (1, 2), (1, 2, 3)], [0, 1, 2, 1, 3], [(1, 1), (1, 2), (0, 0), (1, 2, 3)]), ([(1, 1), (1, 2), (0, 0), (1, 2)], [0, 1, 2, 1], [(1, 1), (1, 2), (0, 0)])])
def test_factorize_tuple_list(self, data, expected_codes, expected_uniques):
    codes, uniques = pd.factorize(data)
    tm.assert_numpy_array_equal(codes, np.array(expected_codes, dtype=np.intp))
    expected_uniques_array = com.asarray_tuplesafe(expected_uniques, dtype=object)
    tm.assert_numpy_array_equal(uniques, expected_uniques_array)