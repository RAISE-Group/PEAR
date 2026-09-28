def test_dataframe(self):
    bts = DataFrame({'a': tm.makeTimeSeries()})
    _, ax = self.plt.subplots()
    bts.plot(ax=ax)
    idx = ax.get_lines()[0].get_xdata()
    tm.assert_index_equal(bts.index.to_period(), PeriodIndex(idx))