def test_get_level_lengths(self):
    index = pd.MultiIndex.from_product([['a', 'b'], [0, 1, 2]])
    expected = {(0, 0): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1}
    result = _get_level_lengths(index)
    tm.assert_dict_equal(result, expected)