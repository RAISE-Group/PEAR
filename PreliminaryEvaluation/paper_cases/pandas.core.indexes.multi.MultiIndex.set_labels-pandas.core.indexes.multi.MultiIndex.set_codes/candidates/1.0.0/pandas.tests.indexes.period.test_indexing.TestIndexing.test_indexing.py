def test_indexing(self):
    index = period_range('1/1/2001', periods=10)
    s = Series(np.random.randn(10), index=index)
    expected = s[index[0]]
    result = s.iat[0]
    assert expected == result