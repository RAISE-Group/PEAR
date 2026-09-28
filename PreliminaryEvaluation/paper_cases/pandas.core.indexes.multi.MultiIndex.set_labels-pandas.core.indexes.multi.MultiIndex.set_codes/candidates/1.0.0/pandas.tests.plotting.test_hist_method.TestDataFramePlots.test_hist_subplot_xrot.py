def test_hist_subplot_xrot(self):
    df = DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3], 'animal': ['pig', 'rabbit', 'pig', 'pig', 'rabbit']})
    axes = _check_plot_works(df.hist, filterwarnings='always', column='length', by='animal', bins=5, xrot=0)
    self._check_ticks_props(axes, xrot=0)