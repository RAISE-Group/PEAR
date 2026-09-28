@pytest.mark.parametrize('data', [np.array([0, 1, 0], dtype='u8'), np.array([-2 ** 63, 1, -2 ** 63], dtype='i8'), np.array(['__nan__', 'foo', '__nan__'], dtype='object')])
def test_parametrized_factorize_na_value_default(self, data):
    codes, uniques = algos.factorize(data)
    expected_uniques = data[[0, 1]]
    expected_codes = np.array([0, 1, 0], dtype=np.intp)
    tm.assert_numpy_array_equal(codes, expected_codes)
    tm.assert_numpy_array_equal(uniques, expected_uniques)