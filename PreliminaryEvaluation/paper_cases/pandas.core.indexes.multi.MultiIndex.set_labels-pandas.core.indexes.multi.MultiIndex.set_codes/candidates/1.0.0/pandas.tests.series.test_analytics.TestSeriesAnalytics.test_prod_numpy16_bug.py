def test_prod_numpy16_bug(self):
    s = Series([1.0, 1.0, 1.0], index=range(3))
    result = s.prod()
    assert not isinstance(result, Series)