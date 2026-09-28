@pytest.mark.parametrize('method', ['pearson', 'kendall', 'spearman'])
@td.skip_if_no_scipy
def test_corr_scipy_method(self, float_frame, method):
    float_frame['A'][:5] = np.nan
    float_frame['B'][5:10] = np.nan
    correls = float_frame.corr(method=method)
    expected = float_frame['A'].corr(float_frame['C'], method=method)
    tm.assert_almost_equal(correls['A']['C'], expected)