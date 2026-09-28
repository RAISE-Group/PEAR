def test_stat_op_calc(self, float_frame_with_na, mixed_float_frame):

    def count(s):
        return notna(s).sum()

    def nunique(s):
        return len(algorithms.unique1d(s.dropna()))

    def mad(x):
        return np.abs(x - x.mean()).mean()

    def var(x):
        return np.var(x, ddof=1)

    def std(x):
        return np.std(x, ddof=1)

    def sem(x):
        return np.std(x, ddof=1) / np.sqrt(len(x))

    def skewness(x):
        from scipy.stats import skew
        if len(x) < 3:
            return np.nan
        return skew(x, bias=False)

    def kurt(x):
        from scipy.stats import kurtosis
        if len(x) < 4:
            return np.nan
        return kurtosis(x, bias=False)
    assert_stat_op_calc('nunique', nunique, float_frame_with_na, has_skipna=False, check_dtype=False, check_dates=True)
    assert_stat_op_calc('sum', np.sum, mixed_float_frame.astype('float32'), check_dtype=False, check_less_precise=True)
    assert_stat_op_calc('sum', np.sum, float_frame_with_na, skipna_alternative=np.nansum)
    assert_stat_op_calc('mean', np.mean, float_frame_with_na, check_dates=True)
    assert_stat_op_calc('product', np.prod, float_frame_with_na)
    assert_stat_op_calc('mad', mad, float_frame_with_na)
    assert_stat_op_calc('var', var, float_frame_with_na)
    assert_stat_op_calc('std', std, float_frame_with_na)
    assert_stat_op_calc('sem', sem, float_frame_with_na)
    assert_stat_op_calc('count', count, float_frame_with_na, has_skipna=False, check_dtype=False, check_dates=True)
    try:
        from scipy import skew, kurtosis
        assert_stat_op_calc('skew', skewness, float_frame_with_na)
        assert_stat_op_calc('kurt', kurt, float_frame_with_na)
    except ImportError:
        pass