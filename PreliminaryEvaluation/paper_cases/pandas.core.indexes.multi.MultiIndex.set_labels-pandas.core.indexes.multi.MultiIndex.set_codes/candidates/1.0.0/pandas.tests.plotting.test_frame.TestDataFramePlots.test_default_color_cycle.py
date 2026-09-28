def test_default_color_cycle(self):
    import matplotlib.pyplot as plt
    import cycler
    colors = list('rgbk')
    plt.rcParams['axes.prop_cycle'] = cycler.cycler('color', colors)
    df = DataFrame(randn(5, 3))
    ax = df.plot()
    expected = self._unpack_cycler(plt.rcParams)[:3]
    self._check_colors(ax.get_lines(), linecolors=expected)