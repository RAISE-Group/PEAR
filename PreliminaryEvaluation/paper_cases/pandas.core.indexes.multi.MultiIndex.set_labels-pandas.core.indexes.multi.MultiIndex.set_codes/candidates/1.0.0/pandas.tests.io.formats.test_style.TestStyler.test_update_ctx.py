def test_update_ctx(self):
    self.styler._update_ctx(self.attrs)
    expected = {(0, 0): ['color: red'], (1, 0): ['color: blue']}
    assert self.styler.ctx == expected