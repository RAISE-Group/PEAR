def test_in_numeric_groupby(self, data_for_grouping):
    df = pd.DataFrame({'A': [1, 1, 2, 2, 3, 3, 1, 4], 'B': data_for_grouping, 'C': [1, 1, 1, 1, 1, 1, 1, 1]})
    result = df.groupby('A').sum().columns
    if data_for_grouping.dtype._is_numeric:
        expected = pd.Index(['B', 'C'])
    else:
        expected = pd.Index(['C'])
    tm.assert_index_equal(result, expected)