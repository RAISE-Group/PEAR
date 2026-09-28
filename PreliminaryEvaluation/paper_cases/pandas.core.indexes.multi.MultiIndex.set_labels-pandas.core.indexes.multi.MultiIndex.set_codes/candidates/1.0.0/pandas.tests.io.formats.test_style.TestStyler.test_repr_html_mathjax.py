def test_repr_html_mathjax(self):
    assert 'tex2jax_ignore' not in self.styler._repr_html_()
    with pd.option_context('display.html.use_mathjax', False):
        assert 'tex2jax_ignore' in self.styler._repr_html_()