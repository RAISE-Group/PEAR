def test_export(self):
    f = lambda x: 'color: red' if x > 0 else 'color: blue'
    g = lambda x, z: f'color: {z}' if x > 0 else f'color: {z}'
    style1 = self.styler
    style1.applymap(f).applymap(g, z='b').highlight_max()
    result = style1.export()
    style2 = self.df.style
    style2.use(result)
    assert style1._todo == style2._todo
    style2.render()