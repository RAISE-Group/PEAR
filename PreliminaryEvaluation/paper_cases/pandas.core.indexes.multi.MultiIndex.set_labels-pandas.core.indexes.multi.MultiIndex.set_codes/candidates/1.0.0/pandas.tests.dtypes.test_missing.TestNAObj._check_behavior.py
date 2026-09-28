def _check_behavior(self, arr, expected):
    for method in TestNAObj._1d_methods:
        result = getattr(libmissing, method)(arr)
        tm.assert_numpy_array_equal(result, expected)
    arr = np.atleast_2d(arr)
    expected = np.atleast_2d(expected)
    for method in TestNAObj._2d_methods:
        result = getattr(libmissing, method)(arr)
        tm.assert_numpy_array_equal(result, expected)