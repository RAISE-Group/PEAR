def test_repr_html_mathjax(self):
    df = DataFrame([[1, 2], [3, 4]])
    assert 'tex2jax_ignore' not in df._repr_html_()
    with pd.option_context('display.html.use_mathjax', False):
        assert 'tex2jax_ignore' in df._repr_html_()