def test_mixed_freq_hf_first(self):
    idxh = date_range('1/1/1999', periods=365, freq='D')
    idxl = date_range('1/1/1999', periods=12, freq='M')
    high = Series(np.random.randn(len(idxh)), idxh)
    low = Series(np.random.randn(len(idxl)), idxl)
    _, ax = self.plt.subplots()
    high.plot(ax=ax)
    low.plot(ax=ax)
    for l in ax.get_lines():
        assert PeriodIndex(data=l.get_xdata()).freq == 'D'