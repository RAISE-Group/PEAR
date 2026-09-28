@pytest.mark.filterwarnings('ignore:All-NaN:RuntimeWarning')
def test_median(self, float_frame_with_na, int_frame):

    def wrapper(x):
        if isna(x).any():
            return np.nan
        return np.median(x)
    assert_stat_op_calc('median', wrapper, float_frame_with_na, check_dates=True)
    assert_stat_op_calc('median', wrapper, int_frame, check_dtype=False, check_dates=True)