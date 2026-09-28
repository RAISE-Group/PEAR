def test_nat_handling(self):
    _, ax = self.plt.subplots()
    dti = DatetimeIndex(['2015-01-01', NaT, '2015-01-03'])
    s = Series(range(len(dti)), dti)
    s.plot(ax=ax)
    xdata = ax.get_lines()[0].get_xdata()
    assert s.index.min() <= Series(xdata).min()
    assert Series(xdata).max() <= s.index.max()