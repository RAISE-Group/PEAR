def test_int_int(self):
    data = Series([1, 2, 1])
    result = pd.get_dummies(data)
    expected = DataFrame([[1, 0], [0, 1], [1, 0]], columns=[1, 2], dtype=np.uint8)
    tm.assert_frame_equal(result, expected)
    data = Series(pd.Categorical(['a', 'b', 'a']))
    result = pd.get_dummies(data)
    expected = DataFrame([[1, 0], [0, 1], [1, 0]], columns=pd.Categorical(['a', 'b']), dtype=np.uint8)
    tm.assert_frame_equal(result, expected)