def test_getitem_seconds(self):
    didx = pd.date_range(start='2013/01/01 09:00:00', freq='S', periods=4000)
    pidx = period_range(start='2013/01/01 09:00:00', freq='S', periods=4000)
    for idx in [didx, pidx]:
        values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
        for v in values:
            continue
        s = Series(np.random.rand(len(idx)), index=idx)
        tm.assert_series_equal(s['2013/01/01 10:00'], s[3600:3660])
        tm.assert_series_equal(s['2013/01/01 9H'], s[:3600])
        for d in ['2013/01/01', '2013/01', '2013']:
            tm.assert_series_equal(s[d], s)