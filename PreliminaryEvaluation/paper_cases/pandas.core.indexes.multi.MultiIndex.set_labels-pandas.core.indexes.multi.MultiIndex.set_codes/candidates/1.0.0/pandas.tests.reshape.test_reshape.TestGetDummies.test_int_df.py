def test_int_df(self, dtype):
    data = DataFrame({'A': [1, 2, 1], 'B': pd.Categorical(['a', 'b', 'a']), 'C': [1, 2, 1], 'D': [1.0, 2.0, 1.0]})
    columns = ['C', 'D', 'A_1', 'A_2', 'B_a', 'B_b']
    expected = DataFrame([[1, 1.0, 1, 0, 1, 0], [2, 2.0, 0, 1, 0, 1], [1, 1.0, 1, 0, 1, 0]], columns=columns)
    expected[columns[2:]] = expected[columns[2:]].astype(dtype)
    result = pd.get_dummies(data, columns=['A', 'B'], dtype=dtype)
    tm.assert_frame_equal(result, expected)