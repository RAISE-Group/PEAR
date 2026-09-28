@pytest.mark.slow
@td.skip_if_no_scipy
def test_kde_colors_and_styles_subplots(self):
    from matplotlib import cm
    default_colors = self._unpack_cycler(self.plt.rcParams)
    df = DataFrame(randn(5, 5))
    axes = df.plot(kind='kde', subplots=True)
    for ax, c in zip(axes, list(default_colors)):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()
    axes = df.plot(kind='kde', color='k', subplots=True)
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['k'])
    tm.close()
    axes = df.plot(kind='kde', color='red', subplots=True)
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['red'])
    tm.close()
    custom_colors = 'rgcby'
    axes = df.plot(kind='kde', color=custom_colors, subplots=True)
    for ax, c in zip(axes, list(custom_colors)):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()
    rgba_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
    for cmap in ['jet', cm.jet]:
        axes = df.plot(kind='kde', colormap=cmap, subplots=True)
        for ax, c in zip(axes, rgba_colors):
            self._check_colors(ax.get_lines(), linecolors=[c])
        tm.close()
    axes = df.loc[:, [0]].plot(kind='kde', color='DodgerBlue', subplots=True)
    self._check_colors(axes[0].lines, linecolors=['DodgerBlue'])
    axes = df.plot(kind='kde', style='r', subplots=True)
    for ax in axes:
        self._check_colors(ax.get_lines(), linecolors=['r'])
    tm.close()
    styles = list('rgcby')
    axes = df.plot(kind='kde', style=styles, subplots=True)
    for ax, c in zip(axes, styles):
        self._check_colors(ax.get_lines(), linecolors=[c])
    tm.close()