@pytest.mark.slow
def test_subplots_dup_columns(self):
    df = DataFrame(np.random.rand(5, 5), columns=list('aaaaa'))
    axes = df.plot(subplots=True)
    for ax in axes:
        self._check_legend_labels(ax, labels=['a'])
        assert len(ax.lines) == 1
    tm.close()
    axes = df.plot(subplots=True, secondary_y='a')
    for ax in axes:
        self._check_legend_labels(ax, labels=['a'])
        assert len(ax.lines) == 1
    tm.close()
    ax = df.plot(secondary_y='a')
    self._check_legend_labels(ax, labels=['a (right)'] * 5)
    assert len(ax.lines) == 0
    assert len(ax.right_ax.lines) == 5