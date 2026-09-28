def test_range_slice_day(self):
    didx = pd.date_range(start='2013/01/01', freq='D', periods=400)
    pidx = period_range(start='2013/01/01', freq='D', periods=400)
    for idx in [didx, pidx]:
        values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
        for v in values:
            with pytest.raises(TypeError):
                idx[v:]
        s = Series(np.random.rand(len(idx)), index=idx)
        tm.assert_series_equal(s['2013/01/02':], s[1:])
        tm.assert_series_equal(s['2013/01/02':'2013/01/05'], s[1:5])
        tm.assert_series_equal(s['2013/02':], s[31:])
        tm.assert_series_equal(s['2014':], s[365:])
        invalid = ['2013/02/01 9H', '2013/02/01 09:00']
        for v in invalid:
            with pytest.raises(TypeError):
                idx[v:]