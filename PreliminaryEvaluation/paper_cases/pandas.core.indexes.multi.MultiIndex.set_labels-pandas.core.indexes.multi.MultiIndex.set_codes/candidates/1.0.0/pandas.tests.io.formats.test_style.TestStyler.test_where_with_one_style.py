def test_where_with_one_style(self):

    def f(x):
        return x > 0.5
    style1 = 'foo: bar'
    result = self.df.style.where(f, style1)._compute().ctx
    expected = {(r, c): [style1 if f(self.df.loc[row, col]) else ''] for r, row in enumerate(self.df.index) for c, col in enumerate(self.df.columns)}
    assert result == expected