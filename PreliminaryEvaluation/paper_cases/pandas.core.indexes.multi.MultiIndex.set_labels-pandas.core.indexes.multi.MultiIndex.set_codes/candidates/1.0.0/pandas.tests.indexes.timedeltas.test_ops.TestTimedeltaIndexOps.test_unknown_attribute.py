def test_unknown_attribute(self):
    tdi = pd.timedelta_range(start=0, periods=10, freq='1s')
    ts = pd.Series(np.random.normal(size=10), index=tdi)
    assert 'foo' not in ts.__dict__.keys()
    msg = "'Series' object has no attribute 'foo'"
    with pytest.raises(AttributeError, match=msg):
        ts.foo