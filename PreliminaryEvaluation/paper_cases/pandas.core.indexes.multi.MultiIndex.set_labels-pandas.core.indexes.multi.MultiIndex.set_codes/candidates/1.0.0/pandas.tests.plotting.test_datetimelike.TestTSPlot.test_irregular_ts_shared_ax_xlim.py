@pytest.mark.slow
def test_irregular_ts_shared_ax_xlim(self):
    ts = tm.makeTimeSeries()[:20]
    ts_irregular = ts[[1, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 17, 18]]
    _, ax = self.plt.subplots()
    ts_irregular[:5].plot(ax=ax)
    ts_irregular[5:].plot(ax=ax)
    left, right = ax.get_xlim()
    assert left <= ts_irregular.index.min().toordinal()
    assert right >= ts_irregular.index.max().toordinal()