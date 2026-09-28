@pytest.mark.slow
def test_tsplot(self):
    _, ax = self.plt.subplots()
    ts = tm.makeTimeSeries()
    for s in self.period_ser:
        _check_plot_works(s.plot, ax=ax)
    for s in self.datetime_ser:
        _check_plot_works(s.plot, ax=ax)
    _, ax = self.plt.subplots()
    ts.plot(style='k', ax=ax)
    color = (0.0, 0.0, 0.0, 1)
    assert color == ax.get_lines()[0].get_color()