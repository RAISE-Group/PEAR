@pytest.mark.slow
def test_business_freq_convert(self):
    bts = tm.makeTimeSeries(300).asfreq('BM')
    ts = bts.to_period('M')
    _, ax = self.plt.subplots()
    bts.plot(ax=ax)
    assert ax.get_lines()[0].get_xydata()[0, 0] == ts.index[0].ordinal
    idx = ax.get_lines()[0].get_xdata()
    assert PeriodIndex(data=idx).freqstr == 'M'