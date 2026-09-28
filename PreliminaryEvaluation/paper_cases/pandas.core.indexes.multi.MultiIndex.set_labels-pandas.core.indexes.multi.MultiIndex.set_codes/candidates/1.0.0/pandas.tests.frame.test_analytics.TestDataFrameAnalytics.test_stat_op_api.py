def test_stat_op_api(self, float_frame, float_string_frame):
    assert_stat_op_api('count', float_frame, float_string_frame, has_numeric_only=True)
    assert_stat_op_api('sum', float_frame, float_string_frame, has_numeric_only=True)
    assert_stat_op_api('nunique', float_frame, float_string_frame)
    assert_stat_op_api('mean', float_frame, float_string_frame)
    assert_stat_op_api('product', float_frame, float_string_frame)
    assert_stat_op_api('median', float_frame, float_string_frame)
    assert_stat_op_api('min', float_frame, float_string_frame)
    assert_stat_op_api('max', float_frame, float_string_frame)
    assert_stat_op_api('mad', float_frame, float_string_frame)
    assert_stat_op_api('var', float_frame, float_string_frame)
    assert_stat_op_api('std', float_frame, float_string_frame)
    assert_stat_op_api('sem', float_frame, float_string_frame)
    assert_stat_op_api('median', float_frame, float_string_frame)
    try:
        from scipy.stats import skew, kurtosis
        assert_stat_op_api('skew', float_frame, float_string_frame)
        assert_stat_op_api('kurt', float_frame, float_string_frame)
    except ImportError:
        pass