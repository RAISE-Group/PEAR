def test_matplotlib_scatter_datetime64(self):
    df = DataFrame(np.random.RandomState(0).rand(10, 2), columns=['x', 'y'])
    df['time'] = date_range('2018-01-01', periods=10, freq='D')
    fig, ax = self.plt.subplots()
    ax.scatter(x='time', y='y', data=df)
    self.plt.draw()
    label = ax.get_xticklabels()[0]
    if self.mpl_ge_3_0_0:
        expected = '2017-12-08'
    else:
        expected = '2017-12-12'
    assert label.get_text() == expected