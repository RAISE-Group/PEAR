@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor(self, which):
    o = getattr(self, which)
    c = o.rolling
    c(window=2)
    c(window=2, min_periods=1)
    c(window=2, min_periods=1, center=True)
    c(window=2, min_periods=1, center=False)
    with pytest.raises(ValueError):
        c(0)
        c(-1)
    for w in [2.0, 'foo', np.array([2])]:
        with pytest.raises(ValueError):
            c(window=w)
        with pytest.raises(ValueError):
            c(window=2, min_periods=w)
        with pytest.raises(ValueError):
            c(window=2, min_periods=1, center=w)