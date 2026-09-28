def test_update_ctx_flatten_multi_traliing_semi(self):
    attrs = DataFrame({'A': ['color: red; foo: bar;', 'color: blue; foo: baz;']})
    self.styler._update_ctx(attrs)
    expected = {(0, 0): ['color: red', ' foo: bar'], (1, 0): ['color: blue', ' foo: baz']}
    assert self.styler.ctx == expected