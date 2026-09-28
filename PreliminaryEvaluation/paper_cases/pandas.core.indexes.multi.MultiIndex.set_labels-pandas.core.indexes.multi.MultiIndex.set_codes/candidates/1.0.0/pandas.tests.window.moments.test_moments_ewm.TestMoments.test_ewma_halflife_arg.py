def test_ewma_halflife_arg(self):
    A = self.series.ewm(com=13.932726172912965).mean()
    B = self.series.ewm(halflife=10.0).mean()
    tm.assert_almost_equal(A, B)
    with pytest.raises(ValueError):
        self.series.ewm(span=20, halflife=50)
    with pytest.raises(ValueError):
        self.series.ewm(com=9.5, halflife=50)
    with pytest.raises(ValueError):
        self.series.ewm(com=9.5, span=20, halflife=50)
    with pytest.raises(ValueError):
        self.series.ewm()