@pytest.mark.slow
def test_hexbin_cmap(self):
    df = self.hexbin_df
    ax = df.plot.hexbin(x='A', y='B')
    assert ax.collections[0].cmap.name == 'BuGn'
    cm = 'cubehelix'
    ax = df.plot.hexbin(x='A', y='B', colormap=cm)
    assert ax.collections[0].cmap.name == cm