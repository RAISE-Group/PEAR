def test_ffill(self):
    ts = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=tm.makeDateIndex(5))
    ts[2] = np.NaN
    tm.assert_series_equal(ts.ffill(), ts.fillna(method='ffill'))