def test_asarray_homogenous(self):
    df = pd.DataFrame({'A': pd.Categorical([1, 2]), 'B': pd.Categorical([1, 2])})
    result = np.asarray(df)
    expected = np.array([[1, 1], [2, 2]], dtype='object')
    tm.assert_numpy_array_equal(result, expected)