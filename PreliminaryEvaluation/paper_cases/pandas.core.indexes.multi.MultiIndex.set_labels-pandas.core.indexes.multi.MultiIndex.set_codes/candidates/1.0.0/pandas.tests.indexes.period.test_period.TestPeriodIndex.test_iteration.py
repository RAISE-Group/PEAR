def test_iteration(self):
    index = period_range(start='1/1/10', periods=4, freq='B')
    result = list(index)
    assert isinstance(result[0], Period)
    assert result[0].freq == index.freq