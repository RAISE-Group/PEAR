@pytest.mark.slow
def test_axis_share_x(self):
    df = self.hist_df
    ax1, ax2 = df.hist(column='height', by=df.gender, sharex=True)
    assert ax1._shared_x_axes.joined(ax1, ax2)
    assert ax2._shared_x_axes.joined(ax1, ax2)
    assert not ax1._shared_y_axes.joined(ax1, ax2)
    assert not ax2._shared_y_axes.joined(ax1, ax2)