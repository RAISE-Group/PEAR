def test_format_date_axis(self):
    rng = date_range('1/1/2012', periods=12, freq='M')
    df = DataFrame(np.random.randn(len(rng), 3), rng)
    _, ax = self.plt.subplots()
    ax = df.plot(ax=ax)
    xaxis = ax.get_xaxis()
    for l in xaxis.get_ticklabels():
        if len(l.get_text()) > 0:
            assert l.get_rotation() == 30