def test_same_nan_is_in(self):
    comps = [np.nan]
    values = [np.nan]
    expected = np.array([True])
    result = algos.isin(comps, values)
    tm.assert_numpy_array_equal(expected, result)