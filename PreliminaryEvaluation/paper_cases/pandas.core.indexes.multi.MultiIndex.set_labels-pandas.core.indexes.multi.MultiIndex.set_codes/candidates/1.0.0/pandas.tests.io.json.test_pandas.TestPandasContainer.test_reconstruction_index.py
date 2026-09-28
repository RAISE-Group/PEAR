def test_reconstruction_index(self):
    df = DataFrame([[1, 2, 3], [4, 5, 6]])
    result = read_json(df.to_json())
    tm.assert_frame_equal(result, df)
    df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['A', 'B', 'C'])
    result = read_json(df.to_json())
    tm.assert_frame_equal(result, df)