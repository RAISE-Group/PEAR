@pytest.mark.parametrize('x,y,lbl,colors', [('A', ['B'], ['b'], ['red']), ('A', ['B', 'C'], ['b', 'c'], ['red', 'blue']), (0, [1, 2], ['bokeh', 'cython'], ['green', 'yellow'])])
def test_y_listlike(self, x, y, lbl, colors):
    df = DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    _check_plot_works(df.plot, x='A', y=y, label=lbl)
    ax = df.plot(x=x, y=y, label=lbl, color=colors)
    assert len(ax.lines) == len(y)
    self._check_colors(ax.get_lines(), linecolors=colors)