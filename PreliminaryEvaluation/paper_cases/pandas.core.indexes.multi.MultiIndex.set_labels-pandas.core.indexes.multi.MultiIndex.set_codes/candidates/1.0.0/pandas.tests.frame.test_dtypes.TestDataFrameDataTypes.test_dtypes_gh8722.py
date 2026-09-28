def test_dtypes_gh8722(self, float_string_frame):
    float_string_frame['bool'] = float_string_frame['A'] > 0
    result = float_string_frame.dtypes
    expected = Series({k: v.dtype for k, v in float_string_frame.items()}, index=result.index)
    tm.assert_series_equal(result, expected)
    with option_context('use_inf_as_na', True):
        df = DataFrame([[1]])
        result = df.dtypes
        tm.assert_series_equal(result, Series({0: np.dtype('int64')}))