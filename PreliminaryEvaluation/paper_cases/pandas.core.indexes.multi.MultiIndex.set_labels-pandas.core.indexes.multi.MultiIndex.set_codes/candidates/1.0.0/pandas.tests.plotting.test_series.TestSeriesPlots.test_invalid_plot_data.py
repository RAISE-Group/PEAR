@pytest.mark.slow
def test_invalid_plot_data(self):
    s = Series(list('abcd'))
    _, ax = self.plt.subplots()
    for kind in plotting.PlotAccessor._common_kinds:
        msg = 'no numeric data to plot'
        with pytest.raises(TypeError, match=msg):
            s.plot(kind=kind, ax=ax)