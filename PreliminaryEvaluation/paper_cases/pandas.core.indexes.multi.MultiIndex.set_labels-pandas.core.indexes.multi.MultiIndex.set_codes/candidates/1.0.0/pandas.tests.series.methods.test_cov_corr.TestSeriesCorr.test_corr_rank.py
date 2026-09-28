@td.skip_if_no_scipy
def test_corr_rank(self):
    import scipy.stats as stats
    A = tm.makeTimeSeries()
    B = tm.makeTimeSeries()
    A[-5:] = A[:5]
    result = A.corr(B, method='kendall')
    expected = stats.kendalltau(A, B)[0]
    tm.assert_almost_equal(result, expected)
    result = A.corr(B, method='spearman')
    expected = stats.spearmanr(A, B)[0]
    tm.assert_almost_equal(result, expected)
    A = Series([-0.89926396, 0.94209606, -1.03289164, -0.95445587, 0.7691031, -0.06430576, -2.09704447, 0.40660407, -0.89926396, 0.94209606])
    B = Series([-1.01270225, -0.62210117, -1.56895827, 0.59592943, -0.01680292, 1.17258718, -1.06009347, -0.1022206, -0.89076239, 0.89372375])
    kexp = 0.4319297
    sexp = 0.5853767
    tm.assert_almost_equal(A.corr(B, method='kendall'), kexp)
    tm.assert_almost_equal(A.corr(B, method='spearman'), sexp)