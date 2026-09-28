def test_get_level_lengths_un_sorted(self):
    index = pd.MultiIndex.from_arrays([[1, 1, 2, 1], ['a', 'b', 'b', 'd']])
    expected = {(0, 0): 2, (0, 2): 1, (0, 3): 1, (1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1}
    result = _get_level_lengths(index)
    tm.assert_dict_equal(result, expected)