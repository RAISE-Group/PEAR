@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor(self, which):
    o = getattr(self, which)
    c = o.expanding
    c(min_periods=1)
    c(min_periods=1, center=True)
    c(min_periods=1, center=False)
    for w in [2.0, 'foo', np.array([2])]:
        with pytest.raises(ValueError):
            c(min_periods=w)
        with pytest.raises(ValueError):
            c(min_periods=1, center=w)