def test_apply_reduce_rows_to_dict(self):
    data = pd.DataFrame([[1, 2], [3, 4]])
    expected = pd.Series([{0: 1, 1: 3}, {0: 2, 1: 4}])
    result = data.apply(dict)
    tm.assert_series_equal(result, expected)