def test_precision(self):
    with pd.option_context('display.precision', 10):
        s = Styler(self.df)
    assert s.precision == 10
    s = Styler(self.df, precision=2)
    assert s.precision == 2
    s2 = s.set_precision(4)
    assert s is s2
    assert s.precision == 4