def test_truncate_nonsortedindex(self):
    s = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[5, 3, 2, 9, 0])
    msg = 'truncate requires a sorted index'
    with pytest.raises(ValueError, match=msg):
        s.truncate(before=3, after=9)
    rng = pd.date_range('2011-01-01', '2012-01-01', freq='W')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    msg = 'truncate requires a sorted index'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending=False).truncate(before='2011-11', after='2011-12')