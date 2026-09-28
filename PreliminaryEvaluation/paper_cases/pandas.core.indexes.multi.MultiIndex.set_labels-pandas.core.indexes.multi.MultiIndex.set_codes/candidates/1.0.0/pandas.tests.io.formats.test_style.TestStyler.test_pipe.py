def test_pipe(self):

    def set_caption_from_template(styler, a, b):
        return styler.set_caption(f'Dataframe with a = {a} and b = {b}')
    styler = self.df.style.pipe(set_caption_from_template, 'A', b='B')
    assert 'Dataframe with a = A and b = B' in styler.render()

    def f(a, b, styler):
        return (a, b, styler)
    styler = self.df.style
    result = styler.pipe((f, 'styler'), a=1, b=2)
    assert result == (1, 2, styler)