def test_render_double(self):
    df = pd.DataFrame({'A': [0, 1]})
    style = lambda x: pd.Series(['color: red; border: 1px', 'color: blue; border: 2px'], name=x.name)
    s = Styler(df, uuid='AB').apply(style)
    s.render()