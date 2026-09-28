def test_table_styles(self):
    style = [{'selector': 'th', 'props': [('foo', 'bar')]}]
    styler = Styler(self.df, table_styles=style)
    result = ' '.join(styler.render().split())
    assert 'th { foo: bar; }' in result
    styler = self.df.style
    result = styler.set_table_styles(style)
    assert styler is result
    assert styler.table_styles == style