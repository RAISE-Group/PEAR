def test_categorical_from_codes(self):
    vals = np.array([0, 1, 2, 0])
    cats = ['a', 'b', 'c']
    Sd = Series(Categorical(1).from_codes(vals, cats))
    St = Series(Categorical(1).from_codes(np.array([0, 1]), cats))
    expected = np.array([True, True, False, True])
    result = algos.isin(Sd, St)
    tm.assert_numpy_array_equal(expected, result)