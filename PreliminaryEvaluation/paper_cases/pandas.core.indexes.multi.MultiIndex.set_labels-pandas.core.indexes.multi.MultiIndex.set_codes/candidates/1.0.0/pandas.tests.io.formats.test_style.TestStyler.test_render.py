def test_render(self):
    df = pd.DataFrame({'A': [0, 1]})
    style = lambda x: pd.Series(['color: red', 'color: blue'], name=x.name)
    s = Styler(df, uuid='AB').apply(style)
    s.render()