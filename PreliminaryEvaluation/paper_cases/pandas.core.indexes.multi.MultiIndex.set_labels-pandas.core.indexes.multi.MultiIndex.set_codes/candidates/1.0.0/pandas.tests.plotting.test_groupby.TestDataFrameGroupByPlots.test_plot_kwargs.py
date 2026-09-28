def test_plot_kwargs(self):
    df = DataFrame({'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 2, 1], 'z': list('ababa')})
    res = df.groupby('z').plot(kind='scatter', x='x', y='y')
    assert len(res['a'].collections) == 1
    res = df.groupby('z').plot.scatter(x='x', y='y')
    assert len(res['a'].collections) == 1