def test_constructor_list_of_series_aligned_index(self):
    series = [pd.Series(i, index=['b', 'a', 'c'], name=str(i)) for i in range(3)]
    result = pd.DataFrame(series)
    expected = pd.DataFrame({'b': [0, 1, 2], 'a': [0, 1, 2], 'c': [0, 1, 2]}, columns=['b', 'a', 'c'], index=['0', '1', '2'])
    tm.assert_frame_equal(result, expected)