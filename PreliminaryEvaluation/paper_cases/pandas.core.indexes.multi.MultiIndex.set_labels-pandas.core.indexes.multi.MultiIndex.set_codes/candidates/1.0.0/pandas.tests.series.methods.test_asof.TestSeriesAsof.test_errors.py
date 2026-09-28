def test_errors(self):
    s = Series([1, 2, 3], index=[Timestamp('20130101'), Timestamp('20130103'), Timestamp('20130102')])
    assert not s.index.is_monotonic
    with pytest.raises(ValueError):
        s.asof(s.index[0])
    N = 10
    rng = date_range('1/1/1990', periods=N, freq='53s')
    s = Series(np.random.randn(N), index=rng)
    with pytest.raises(ValueError):
        s.asof(s.index[0], subset='foo')