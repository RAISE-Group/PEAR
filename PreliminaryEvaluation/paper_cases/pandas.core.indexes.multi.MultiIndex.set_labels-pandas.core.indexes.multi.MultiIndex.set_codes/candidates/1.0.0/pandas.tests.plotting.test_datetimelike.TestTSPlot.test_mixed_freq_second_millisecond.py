@pytest.mark.slow
def test_mixed_freq_second_millisecond(self):
    idxh = date_range('2014-07-01 09:00', freq='S', periods=50)
    idxl = date_range('2014-07-01 09:00', freq='100L', periods=500)
    high = Series(np.random.randn(len(idxh)), idxh)
    low = Series(np.random.randn(len(idxl)), idxl)
    _, ax = self.plt.subplots()
    high.plot(ax=ax)
    low.plot(ax=ax)
    assert len(ax.get_lines()) == 2
    for l in ax.get_lines():
        assert PeriodIndex(data=l.get_xdata()).freq == 'L'
    tm.close()
    _, ax = self.plt.subplots()
    low.plot(ax=ax)
    high.plot(ax=ax)
    assert len(ax.get_lines()) == 2
    for l in ax.get_lines():
        assert PeriodIndex(data=l.get_xdata()).freq == 'L'