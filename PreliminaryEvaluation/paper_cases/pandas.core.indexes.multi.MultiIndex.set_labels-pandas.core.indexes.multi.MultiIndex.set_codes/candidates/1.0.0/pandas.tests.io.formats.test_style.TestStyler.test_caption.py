def test_caption(self):
    styler = Styler(self.df, caption='foo')
    result = styler.render()
    assert all(['caption' in result, 'foo' in result])
    styler = self.df.style
    result = styler.set_caption('baz')
    assert styler is result
    assert styler.caption == 'baz'