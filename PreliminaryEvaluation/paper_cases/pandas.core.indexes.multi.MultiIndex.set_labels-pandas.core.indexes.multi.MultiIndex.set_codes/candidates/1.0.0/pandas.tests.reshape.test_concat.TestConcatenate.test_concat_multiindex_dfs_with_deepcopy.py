def test_concat_multiindex_dfs_with_deepcopy(self):
    from copy import deepcopy
    example_multiindex1 = pd.MultiIndex.from_product([['a'], ['b']])
    example_dataframe1 = pd.DataFrame([0], index=example_multiindex1)
    example_multiindex2 = pd.MultiIndex.from_product([['a'], ['c']])
    example_dataframe2 = pd.DataFrame([1], index=example_multiindex2)
    example_dict = {'s1': example_dataframe1, 's2': example_dataframe2}
    expected_index = pd.MultiIndex(levels=[['s1', 's2'], ['a'], ['b', 'c']], codes=[[0, 1], [0, 0], [0, 1]], names=['testname', None, None])
    expected = pd.DataFrame([[0], [1]], index=expected_index)
    result_copy = pd.concat(deepcopy(example_dict), names=['testname'])
    tm.assert_frame_equal(result_copy, expected)
    result_no_copy = pd.concat(example_dict, names=['testname'])
    tm.assert_frame_equal(result_no_copy, expected)