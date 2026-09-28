@pytest.mark.slow
def test_mixed_freq_lf_first(self):
    idxh = date_range('1/1/1999', periods=365, freq='D')
    idxl = date_range('1/1/1999', periods=12, freq='M')
    high = Series(np.random.randn(len(idxh)), idxh)
    low = Series(np.random.randn(len(idxl)), idxl)
    _, ax = self.plt.subplots()
    low.plot(legend=True, ax=ax)
    high.plot(legend=True, ax=ax)
    for l in ax.get_lines():
        assert PeriodIndex(data=l.get_xdata()).freq == 'D'
    leg = ax.get_legend()
    assert len(leg.texts) == 2
    self.plt.close(ax.get_figure())
    idxh = date_range('1/1/1999', periods=240, freq='T')
    idxl = date_range('1/1/1999', periods=4, freq='H')
    high = Series(np.random.randn(len(idxh)), idxh)
    low = Series(np.random.randn(len(idxl)), idxl)
    _, ax = self.plt.subplots()
    low.plot(ax=ax)
    high.plot(ax=ax)
    for l in ax.get_lines():
        assert PeriodIndex(data=l.get_xdata()).freq == 'T'