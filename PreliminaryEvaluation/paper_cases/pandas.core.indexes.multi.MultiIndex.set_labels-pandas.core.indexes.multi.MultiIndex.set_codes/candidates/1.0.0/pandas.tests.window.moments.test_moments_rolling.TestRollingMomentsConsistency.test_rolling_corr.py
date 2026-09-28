def test_rolling_corr(self):
    A = self.series
    B = A + randn(len(A))
    result = A.rolling(window=50, min_periods=25).corr(B)
    tm.assert_almost_equal(result[-1], np.corrcoef(A[-50:], B[-50:])[0, 1])
    a = tm.makeTimeSeries()
    b = tm.makeTimeSeries()
    a[:5] = np.nan
    b[:10] = np.nan
    result = a.rolling(window=len(a), min_periods=1).corr(b)
    tm.assert_almost_equal(result[-1], a.corr(b))