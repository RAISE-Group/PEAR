def test_partially_invalid_plot_data(self):
    s = Series(['a', 'b', 1.0, 2])
    _, ax = self.plt.subplots()
    for kind in plotting.PlotAccessor._common_kinds:
        msg = 'no numeric data to plot'
        with pytest.raises(TypeError, match=msg):
            s.plot(kind=kind, ax=ax)