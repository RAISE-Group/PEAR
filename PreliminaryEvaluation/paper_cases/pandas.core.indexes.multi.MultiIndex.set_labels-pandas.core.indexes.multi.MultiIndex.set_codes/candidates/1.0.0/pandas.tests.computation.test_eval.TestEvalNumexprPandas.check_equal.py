def check_equal(self, result, expected):
    if isinstance(result, DataFrame):
        tm.assert_frame_equal(result, expected)
    elif isinstance(result, Series):
        tm.assert_series_equal(result, expected)
    elif isinstance(result, np.ndarray):
        tm.assert_numpy_array_equal(result, expected)
    else:
        assert result == expected