@pytest.mark.slow
def test_plot_scatter(self):
    df = DataFrame(randn(6, 4), index=list(string.ascii_letters[:6]), columns=['x', 'y', 'z', 'four'])
    _check_plot_works(df.plot.scatter, x='x', y='y')
    _check_plot_works(df.plot.scatter, x=1, y=2)
    with pytest.raises(TypeError):
        df.plot.scatter(x='x')
    with pytest.raises(TypeError):
        df.plot.scatter(y='y')
    axes = df.plot(x='x', y='y', kind='scatter', subplots=True)
    self._check_axes_shape(axes, axes_num=1, layout=(1, 1))