@pytest.mark.parametrize('interpolation', ['linear', 'lower', 'higher', 'midpoint', 'nearest'])
def test_rolling_quantile(self, interpolation):
    g = self.frame.groupby('A')
    r = g.rolling(window=4)
    result = r.quantile(0.4, interpolation=interpolation)
    expected = g.apply(lambda x: x.rolling(4).quantile(0.4, interpolation=interpolation))
    tm.assert_frame_equal(result, expected)