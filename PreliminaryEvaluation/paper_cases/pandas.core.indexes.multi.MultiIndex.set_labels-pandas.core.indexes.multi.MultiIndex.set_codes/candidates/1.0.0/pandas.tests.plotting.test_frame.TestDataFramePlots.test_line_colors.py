@pytest.mark.slow
def test_line_colors(self):
    from matplotlib import cm
    custom_colors = 'rgcby'
    df = DataFrame(randn(5, 5))
    ax = df.plot(color=custom_colors)
    self._check_colors(ax.get_lines(), linecolors=custom_colors)
    tm.close()
    ax2 = df.plot(color=custom_colors)
    lines2 = ax2.get_lines()
    for l1, l2 in zip(ax.get_lines(), lines2):
        assert l1.get_color() == l2.get_color()
    tm.close()
    ax = df.plot(colormap='jet')
    rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
    self._check_colors(ax.get_lines(), linecolors=rgba_colors)
    tm.close()
    ax = df.plot(colormap=cm.jet)
    rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
    self._check_colors(ax.get_lines(), linecolors=rgba_colors)
    tm.close()
    ax = df.loc[:, [0]].plot(color='DodgerBlue')
    self._check_colors(ax.lines, linecolors=['DodgerBlue'])
    ax = df.plot(color='red')
    self._check_colors(ax.get_lines(), linecolors=['red'] * 5)
    tm.close()
    custom_colors = ['#FF0000', '#0000FF', '#FFFF00', '#000000', '#FFFFFF']
    ax = df.plot(color=custom_colors)
    self._check_colors(ax.get_lines(), linecolors=custom_colors)
    tm.close()
    with pytest.raises(ValueError):
        custom_colors = ['#F00', '#00F', '#FF0', '#000', '#FFF']
        _check_plot_works(df.plot, color=custom_colors)