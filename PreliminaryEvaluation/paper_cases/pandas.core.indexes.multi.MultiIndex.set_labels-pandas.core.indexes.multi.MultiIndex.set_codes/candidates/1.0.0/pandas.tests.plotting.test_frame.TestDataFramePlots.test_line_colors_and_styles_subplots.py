@pytest.mark.slow
def test_line_colors_and_styles_subplots(self):
    from matplotlib import cm
    default_colors = self._unpack_cycler(self.plt.rcParams)
    df = DataFrame(randn(5, 5))
    axes = df.plot(subplots=True)
    for ax, c in zip(axes, list(default_colors)):
        c = [c]
        self._check_colors(ax.get_lines(), linecolors=c)
    tm.close()
    axes = df.plot(subplots=True, color='k')
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['k'])
    tm.close()
    axes = df.plot(subplots=True, color='green')
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['green'])
    tm.close()
    custom_colors = 'rgcby'
    axes = df.plot(color=custom_colors, subplots=True)
    for ax, c in zip(axes, list(custom_colors)):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()
    axes = df.plot(color=list(custom_colors), subplots=True)
    for ax, c in zip(axes, list(custom_colors)):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()
    custom_colors = ['#FF0000', '#0000FF', '#FFFF00', '#000000', '#FFFFFF']
    axes = df.plot(color=custom_colors, subplots=True)
    for ax, c in zip(axes, list(custom_colors)):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()
    with pytest.raises(ValueError):
        custom_colors = ['#F00', '#00F', '#FF0', '#000', '#FFF']
        with tm.assert_produces_warning(UserWarning):
            _check_plot_works(df.plot, color=custom_colors, subplots=True)
    rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
    for cmap in ['jet', cm.jet]:
        axes = df.plot(colormap=cmap, subplots=True)
        for ax, c in zip(axes, rgba_colors):
            self._check_colors(ax.get_lines(), linecolors=[c])
        tm.close()
    axes = df.loc[:, [0]].plot(color='DodgerBlue', subplots=True)
    self._check_colors(axes[0].lines, linecolors=['DodgerBlue'])
    axes = df.plot(style='r', subplots=True)
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['r'])
    tm.close()
    styles = list('rgcby')
    axes = df.plot(style=styles, subplots=True)
    for ax, c in zip(axes, styles):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()