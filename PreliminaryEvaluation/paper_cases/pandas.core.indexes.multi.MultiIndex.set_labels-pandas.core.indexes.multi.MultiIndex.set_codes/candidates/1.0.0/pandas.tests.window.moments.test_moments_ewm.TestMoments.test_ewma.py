def test_ewma(self):
    self._check_ew(name='mean')
    vals = pd.Series(np.zeros(1000))
    vals[5] = 1
    result = vals.ewm(span=100, adjust=False).mean().sum()
    assert np.abs(result - 1) < 0.01