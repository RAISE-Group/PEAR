@pytest.mark.slow
def test_hist_df_with_nonnumerics(self):
    with tm.RNGContext(1):
        df = DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
    df['E'] = ['x', 'y'] * 5
    _, ax = self.plt.subplots()
    ax = df.plot.hist(bins=5, ax=ax)
    assert len(ax.patches) == 20
    _, ax = self.plt.subplots()
    ax = df.plot.hist(ax=ax)
    assert len(ax.patches) == 40