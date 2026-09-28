def test_uuid(self):
    styler = Styler(self.df, uuid='abc123')
    result = styler.render()
    assert 'abc123' in result
    styler = self.df.style
    result = styler.set_uuid('aaa')
    assert result is styler
    assert result.uuid == 'aaa'