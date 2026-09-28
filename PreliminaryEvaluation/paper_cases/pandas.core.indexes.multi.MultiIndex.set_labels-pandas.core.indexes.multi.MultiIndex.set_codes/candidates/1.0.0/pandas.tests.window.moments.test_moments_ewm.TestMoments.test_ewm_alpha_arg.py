def test_ewm_alpha_arg(self):
    s = self.series
    with pytest.raises(ValueError):
        s.ewm()
    with pytest.raises(ValueError):
        s.ewm(com=10.0, alpha=0.5)
    with pytest.raises(ValueError):
        s.ewm(span=10.0, alpha=0.5)
    with pytest.raises(ValueError):
        s.ewm(halflife=10.0, alpha=0.5)