def test_intercept_astype_object(self):
    expected = self.series.astype('object')
    df = DataFrame({'a': self.series, 'b': np.random.randn(len(self.series))})
    result = df.values.squeeze()
    assert (result[:, 0] == expected.values).all()
    df = DataFrame({'a': self.series, 'b': ['foo'] * len(self.series)})
    result = df.values.squeeze()
    assert (result[:, 0] == expected.values).all()