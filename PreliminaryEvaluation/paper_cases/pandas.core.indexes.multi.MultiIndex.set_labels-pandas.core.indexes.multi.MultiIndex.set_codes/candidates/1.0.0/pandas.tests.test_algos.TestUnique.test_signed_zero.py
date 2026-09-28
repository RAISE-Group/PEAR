def test_signed_zero(self):
    a = np.array([-0.0, 0.0])
    result = pd.unique(a)
    expected = np.array([-0.0])
    tm.assert_numpy_array_equal(result, expected)