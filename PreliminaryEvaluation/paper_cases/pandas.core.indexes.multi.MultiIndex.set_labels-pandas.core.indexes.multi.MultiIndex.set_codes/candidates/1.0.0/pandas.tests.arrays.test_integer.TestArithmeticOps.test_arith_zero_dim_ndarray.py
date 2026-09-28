@pytest.mark.parametrize('other', [0, 0.5])
def test_arith_zero_dim_ndarray(self, other):
    arr = integer_array([1, None, 2])
    result = arr + np.array(other)
    expected = arr + other
    tm.assert_equal(result, expected)