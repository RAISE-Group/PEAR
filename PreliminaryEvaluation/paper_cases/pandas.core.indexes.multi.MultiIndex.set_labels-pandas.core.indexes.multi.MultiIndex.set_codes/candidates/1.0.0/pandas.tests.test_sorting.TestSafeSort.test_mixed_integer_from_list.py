def test_mixed_integer_from_list(self):
    values = ['b', 1, 0, 'a', 0, 'b']
    result = safe_sort(values)
    expected = np.array([0, 0, 1, 'a', 'b', 'b'], dtype=object)
    tm.assert_numpy_array_equal(result, expected)