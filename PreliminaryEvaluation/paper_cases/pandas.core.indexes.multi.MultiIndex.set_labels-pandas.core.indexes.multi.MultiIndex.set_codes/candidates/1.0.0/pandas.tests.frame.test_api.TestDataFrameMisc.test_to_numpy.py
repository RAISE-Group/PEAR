def test_to_numpy(self):
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4.5]})
    expected = np.array([[1, 3], [2, 4.5]])
    result = df.to_numpy()
    tm.assert_numpy_array_equal(result, expected)