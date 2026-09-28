def test_ewma_span_com_args(self):
    A = self.series.ewm(com=9.5).mean()
    B = self.series.ewm(span=20).mean()
    tm.assert_almost_equal(A, B)
    with pytest.raises(ValueError):
        self.series.ewm(com=9.5, span=20)
    with pytest.raises(ValueError):
        self.series.ewm().mean()