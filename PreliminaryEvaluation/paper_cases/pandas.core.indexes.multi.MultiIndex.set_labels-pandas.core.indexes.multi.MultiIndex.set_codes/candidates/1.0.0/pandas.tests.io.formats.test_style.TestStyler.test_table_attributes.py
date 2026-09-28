def test_table_attributes(self):
    attributes = 'class="foo" data-bar'
    styler = Styler(self.df, table_attributes=attributes)
    result = styler.render()
    assert 'class="foo" data-bar' in result
    result = self.df.style.set_table_attributes(attributes).render()
    assert 'class="foo" data-bar' in result