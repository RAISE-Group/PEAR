def test_iloc_array_not_mutating_negative_indices(self):
    array_with_neg_numbers = np.array([1, 2, -1])
    array_copy = array_with_neg_numbers.copy()
    df = pd.DataFrame({'A': [100, 101, 102], 'B': [103, 104, 105], 'C': [106, 107, 108]}, index=[1, 2, 3])
    df.iloc[array_with_neg_numbers]
    tm.assert_numpy_array_equal(array_with_neg_numbers, array_copy)
    df.iloc[:, array_with_neg_numbers]
    tm.assert_numpy_array_equal(array_with_neg_numbers, array_copy)