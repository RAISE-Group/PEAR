def test_deepcopy(self):
    s2 = copy.deepcopy(self.styler)
    assert self.styler is not s2
    assert self.styler.ctx is not s2.ctx
    assert self.styler._todo is not s2._todo
    self.styler._update_ctx(self.attrs)
    self.styler.highlight_max()
    assert self.styler.ctx != s2.ctx
    assert s2._todo == []
    assert self.styler._todo != s2._todo