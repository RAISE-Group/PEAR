def test_clear(self):
    s = self.df.style.highlight_max()._compute()
    assert len(s.ctx) > 0
    assert len(s._todo) > 0
    s.clear()
    assert len(s.ctx) == 0
    assert len(s._todo) == 0