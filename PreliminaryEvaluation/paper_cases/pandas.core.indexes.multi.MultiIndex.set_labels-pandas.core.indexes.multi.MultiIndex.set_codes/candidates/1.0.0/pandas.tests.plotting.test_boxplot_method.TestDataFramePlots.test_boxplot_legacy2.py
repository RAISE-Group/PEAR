@pytest.mark.slow
def test_boxplot_legacy2(self):
    df = DataFrame(np.random.rand(10, 2), columns=['Col1', 'Col2'])
    df['X'] = Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
    df['Y'] = Series(['A'] * 10)
    with tm.assert_produces_warning(UserWarning):
        _check_plot_works(df.boxplot, by='X')
    fig, ax = self.plt.subplots()
    axes = df.boxplot('Col1', by='X', ax=ax)
    ax_axes = ax.axes
    assert ax_axes is axes
    fig, ax = self.plt.subplots()
    axes = df.groupby('Y').boxplot(ax=ax, return_type='axes')
    ax_axes = ax.axes
    assert ax_axes is axes['A']
    fig, ax = self.plt.subplots()
    with tm.assert_produces_warning(UserWarning):
        axes = df.boxplot(column=['Col1', 'Col2'], by='X', ax=ax, return_type='axes')
    assert axes['Col1'].get_figure() is fig
    fig, ax = self.plt.subplots()
    d = df.boxplot(ax=ax, return_type='dict')
    lines = list(itertools.chain.from_iterable(d.values()))
    assert len(ax.get_lines()) == len(lines)