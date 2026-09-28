@td.skip_if_no_scipy
def test_corr_non_numeric(self, float_frame, float_string_frame):
    float_frame['A'][:5] = np.nan
    float_frame['B'][5:10] = np.nan
    result = float_string_frame.corr()
    expected = float_string_frame.loc[:, ['A', 'B', 'C', 'D']].corr()
    tm.assert_frame_equal(result, expected)