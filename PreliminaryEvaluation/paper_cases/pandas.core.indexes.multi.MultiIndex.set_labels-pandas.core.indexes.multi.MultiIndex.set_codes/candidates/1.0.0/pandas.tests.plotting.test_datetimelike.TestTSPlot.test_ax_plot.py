@pytest.mark.slow
def test_ax_plot(self):
    x = date_range(start='2012-01-02', periods=10, freq='D')
    y = list(range(len(x)))
    _, ax = self.plt.subplots()
    lines = ax.plot(x, y, label='Y')
    tm.assert_index_equal(DatetimeIndex(lines[0].get_xdata()), x)