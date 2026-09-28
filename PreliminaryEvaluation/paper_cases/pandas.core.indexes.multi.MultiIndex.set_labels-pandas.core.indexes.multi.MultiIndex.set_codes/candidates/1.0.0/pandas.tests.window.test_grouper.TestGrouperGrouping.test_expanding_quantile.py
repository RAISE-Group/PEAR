@pytest.mark.parametrize('interpolation', ['linear', 'lower', 'higher', 'midpoint', 'nearest'])
def test_expanding_quantile(self, interpolation):
    g = self.frame.groupby('A')
    r = g.expanding()
    result = r.quantile(0.4, interpolation=interpolation)
    expected = g.apply(lambda x: x.expanding().quantile(0.4, interpolation=interpolation))
    tm.assert_frame_equal(result, expected)