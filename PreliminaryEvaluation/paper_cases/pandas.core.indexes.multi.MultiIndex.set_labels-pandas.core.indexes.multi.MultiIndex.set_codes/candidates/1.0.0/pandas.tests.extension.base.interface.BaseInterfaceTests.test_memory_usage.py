def test_memory_usage(self, data):
    s = pd.Series(data)
    result = s.memory_usage(index=False)
    assert result == s.nbytes