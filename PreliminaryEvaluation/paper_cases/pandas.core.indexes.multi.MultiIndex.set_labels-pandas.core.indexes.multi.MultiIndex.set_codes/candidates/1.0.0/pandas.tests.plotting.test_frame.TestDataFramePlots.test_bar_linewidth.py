@pytest.mark.slow
def test_bar_linewidth(self):
    df = DataFrame(randn(5, 5))
    ax = df.plot.bar(linewidth=2)
    for r in ax.patches:
        assert r.get_linewidth() == 2
    ax = df.plot.bar(stacked=True, linewidth=2)
    for r in ax.patches:
        assert r.get_linewidth() == 2
    axes = df.plot.bar(linewidth=2, subplots=True)
    self._check_axes_shape(axes, axes_num=5, layout=(5, 1))
    for ax in axes:
        for r in ax.patches:
            assert r.get_linewidth() == 2