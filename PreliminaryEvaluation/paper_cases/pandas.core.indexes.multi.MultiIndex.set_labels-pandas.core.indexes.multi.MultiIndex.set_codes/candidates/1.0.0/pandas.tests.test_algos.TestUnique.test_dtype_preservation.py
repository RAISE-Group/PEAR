def test_dtype_preservation(self, any_numpy_dtype):
    if any_numpy_dtype in BYTES_DTYPES + STRING_DTYPES:
        pytest.skip('skip string dtype')
    elif is_integer_dtype(any_numpy_dtype):
        data = [1, 2, 2]
        uniques = [1, 2]
    elif is_float_dtype(any_numpy_dtype):
        data = [1, 2, 2]
        uniques = [1.0, 2.0]
    elif is_complex_dtype(any_numpy_dtype):
        data = [complex(1, 0), complex(2, 0), complex(2, 0)]
        uniques = [complex(1, 0), complex(2, 0)]
    elif is_bool_dtype(any_numpy_dtype):
        data = [True, True, False]
        uniques = [True, False]
    elif is_object_dtype(any_numpy_dtype):
        data = ['A', 'B', 'B']
        uniques = ['A', 'B']
    else:
        data = [1, 2, 2]
        uniques = [1, 2]
    result = Series(data, dtype=any_numpy_dtype).unique()
    expected = np.array(uniques, dtype=any_numpy_dtype)
    tm.assert_numpy_array_equal(result, expected)