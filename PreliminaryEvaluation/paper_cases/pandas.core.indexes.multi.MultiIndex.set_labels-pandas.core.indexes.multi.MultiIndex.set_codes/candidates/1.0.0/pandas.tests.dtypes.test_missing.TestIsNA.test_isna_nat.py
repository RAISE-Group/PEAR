def test_isna_nat(self):
    result = isna([NaT])
    exp = np.array([True])
    tm.assert_numpy_array_equal(result, exp)
    result = isna(np.array([NaT], dtype=object))
    exp = np.array([True])
    tm.assert_numpy_array_equal(result, exp)