@pytest.mark.slow
def test_no_color_bar(self):
    df = self.hexbin_df
    ax = df.plot.hexbin(x='A', y='B', colorbar=None)
    assert ax.collections[0].colorbar is None