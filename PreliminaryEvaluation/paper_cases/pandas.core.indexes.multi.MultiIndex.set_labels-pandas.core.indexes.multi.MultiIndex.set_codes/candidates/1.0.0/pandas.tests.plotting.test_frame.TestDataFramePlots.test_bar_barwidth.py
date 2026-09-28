@pytest.mark.slow
def test_bar_barwidth(self):
    df = DataFrame(randn(5, 5))
    width = 0.9
    ax = df.plot.bar(width=width)
    for r in ax.patches:
        assert r.get_width() == width / len(df.columns)
    ax = df.plot.bar(stacked=True, width=width)
    for r in ax.patches:
        assert r.get_width() == width
    ax = df.plot.barh(width=width)
    for r in ax.patches:
        assert r.get_height() == width / len(df.columns)
    ax = df.plot.barh(stacked=True, width=width)
    for r in ax.patches:
        assert r.get_height() == width
    axes = df.plot.bar(width=width, subplots=True)
    for ax in axes:
        for r in ax.patches:
            assert r.get_width() == width
    axes = df.plot.barh(width=width, subplots=True)
    for ax in axes:
        for r in ax.patches:
            assert r.get_height() == width