@pytest.mark.slow
def test_hist_kwargs(self):
    _, ax = self.plt.subplots()
    ax = self.ts.plot.hist(bins=5, ax=ax)
    assert len(ax.patches) == 5
    self._check_text_labels(ax.yaxis.get_label(), 'Frequency')
    tm.close()
    _, ax = self.plt.subplots()
    ax = self.ts.plot.hist(orientation='horizontal', ax=ax)
    self._check_text_labels(ax.xaxis.get_label(), 'Frequency')
    tm.close()
    _, ax = self.plt.subplots()
    ax = self.ts.plot.hist(align='left', stacked=True, ax=ax)
    tm.close()