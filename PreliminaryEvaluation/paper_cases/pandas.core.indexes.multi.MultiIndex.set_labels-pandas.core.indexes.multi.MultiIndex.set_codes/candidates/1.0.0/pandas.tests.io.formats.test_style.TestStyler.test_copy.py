def test_copy(self):
    s2 = copy.copy(self.styler)
    assert self.styler is not s2
    assert self.styler.ctx is s2.ctx
    assert self.styler._todo is s2._todo
    self.styler._update_ctx(self.attrs)
    self.styler.highlight_max()
    assert self.styler.ctx == s2.ctx
    assert self.styler._todo == s2._todo