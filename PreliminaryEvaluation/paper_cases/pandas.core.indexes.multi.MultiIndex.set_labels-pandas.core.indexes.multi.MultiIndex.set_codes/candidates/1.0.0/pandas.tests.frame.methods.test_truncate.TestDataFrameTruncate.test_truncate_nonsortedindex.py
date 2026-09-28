def test_truncate_nonsortedindex(self):
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e']}, index=[5, 3, 2, 9, 0])
    msg = 'truncate requires a sorted index'
    with pytest.raises(ValueError, match=msg):
        df.truncate(before=3, after=9)
    rng = pd.date_range('2011-01-01', '2012-01-01', freq='W')
    ts = pd.DataFrame({'A': np.random.randn(len(rng)), 'B': np.random.randn(len(rng))}, index=rng)
    msg = 'truncate requires a sorted index'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values('A', ascending=False).truncate(before='2011-11', after='2011-12')
    df = pd.DataFrame({3: np.random.randn(5), 20: np.random.randn(5), 2: np.random.randn(5), 0: np.random.randn(5)}, columns=[3, 20, 2, 0])
    msg = 'truncate requires a sorted index'
    with pytest.raises(ValueError, match=msg):
        df.truncate(before=2, after=20, axis=1)