@pytest.mark.parametrize('method', ['corr', 'cov'])
def test_flex_binary_frame(self, method):
    series = self.frame[1]
    res = getattr(series.rolling(window=10), method)(self.frame)
    res2 = getattr(self.frame.rolling(window=10), method)(series)
    exp = self.frame.apply(lambda x: getattr(series.rolling(window=10), method)(x))
    tm.assert_frame_equal(res, exp)
    tm.assert_frame_equal(res2, exp)
    frame2 = self.frame.copy()
    frame2.values[:] = np.random.randn(*frame2.shape)
    res3 = getattr(self.frame.rolling(window=10), method)(frame2)
    exp = DataFrame({k: getattr(self.frame[k].rolling(window=10), method)(frame2[k]) for k in self.frame})
    tm.assert_frame_equal(res3, exp)