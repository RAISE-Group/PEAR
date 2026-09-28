@pytest.mark.parametrize('zero, negative', [(0, False), (0.0, False), (-0.0, True)])
def test_divide_by_zero(self, zero, negative):
    a = pd.array([0, 1, -1, None], dtype='Int64')
    result = a / zero
    expected = np.array([np.nan, np.inf, -np.inf, np.nan])
    if negative:
        expected *= -1
    tm.assert_numpy_array_equal(result, expected)