@pytest.mark.slow
def test_hexbin_basic(self):
    df = self.hexbin_df
    ax = df.plot.hexbin(x='A', y='B', gridsize=10)
    assert len(ax.collections) == 1
    axes = df.plot.hexbin(x='A', y='B', subplots=True)
    assert len(axes[0].figure.axes) == 2
    self._check_axes_shape(axes, axes_num=1, layout=(1, 1))