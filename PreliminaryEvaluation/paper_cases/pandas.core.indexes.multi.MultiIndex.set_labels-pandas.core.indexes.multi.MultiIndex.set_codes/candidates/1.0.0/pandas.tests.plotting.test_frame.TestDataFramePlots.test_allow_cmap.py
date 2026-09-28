@pytest.mark.slow
def test_allow_cmap(self):
    df = self.hexbin_df
    ax = df.plot.hexbin(x='A', y='B', cmap='YlGn')
    assert ax.collections[0].cmap.name == 'YlGn'
    with pytest.raises(TypeError):
        df.plot.hexbin(x='A', y='B', cmap='YlGn', colormap='BuGn')