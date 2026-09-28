def test_raise_on_info(self):
    s = Series(np.random.randn(10))
    msg = "'Series' object has no attribute 'info'"
    with pytest.raises(AttributeError, match=msg):
        s.info()