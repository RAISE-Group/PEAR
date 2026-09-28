def test_getitem_day(self):
    didx = pd.date_range(start='2013/01/01', freq='D', periods=400)
    pidx = period_range(start='2013/01/01', freq='D', periods=400)
    for idx in [didx, pidx]:
        values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
        for v in values:
            continue
        s = Series(np.random.rand(len(idx)), index=idx)
        tm.assert_series_equal(s['2013/01'], s[0:31])
        tm.assert_series_equal(s['2013/02'], s[31:59])
        tm.assert_series_equal(s['2014'], s[365:])
        invalid = ['2013/02/01 9H', '2013/02/01 09:00']
        for v in invalid:
            with pytest.raises(KeyError, match=v):
                s[v]