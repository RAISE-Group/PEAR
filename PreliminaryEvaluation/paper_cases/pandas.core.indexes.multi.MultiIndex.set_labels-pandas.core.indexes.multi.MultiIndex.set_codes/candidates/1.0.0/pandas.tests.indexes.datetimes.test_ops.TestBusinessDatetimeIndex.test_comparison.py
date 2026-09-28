def test_comparison(self):
    d = self.rng[10]
    comp = self.rng > d
    assert comp[11]
    assert not comp[9]