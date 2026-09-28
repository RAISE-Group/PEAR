@pytest.mark.parametrize('which', ['series', 'frame'])
def test_constructor(self, which):
    o = getattr(self, which)
    c = o.ewm
    c(com=0.5)
    c(span=1.5)
    c(alpha=0.5)
    c(halflife=0.75)
    c(com=0.5, span=None)
    c(alpha=0.5, com=None)
    c(halflife=0.75, alpha=None)
    with pytest.raises(ValueError):
        c(com=0.5, alpha=0.5)
    with pytest.raises(ValueError):
        c(span=1.5, halflife=0.75)
    with pytest.raises(ValueError):
        c(alpha=0.5, span=1.5)
    with pytest.raises(ValueError):
        c(com=-0.5)
    with pytest.raises(ValueError):
        c(span=0.5)
    with pytest.raises(ValueError):
        c(halflife=0)
    for alpha in (-0.5, 1.5):
        with pytest.raises(ValueError):
            c(alpha=alpha)