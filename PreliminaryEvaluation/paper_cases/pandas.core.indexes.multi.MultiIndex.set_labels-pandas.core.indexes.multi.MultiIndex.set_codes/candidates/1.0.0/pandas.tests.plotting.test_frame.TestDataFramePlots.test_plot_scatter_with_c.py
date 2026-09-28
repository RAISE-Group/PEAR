@pytest.mark.slow
def test_plot_scatter_with_c(self):
    df = DataFrame(randn(6, 4), index=list(string.ascii_letters[:6]), columns=['x', 'y', 'z', 'four'])
    axes = [df.plot.scatter(x='x', y='y', c='z'), df.plot.scatter(x=0, y=1, c=2)]
    for ax in axes:
        assert ax.collections[0].cmap.name == 'Greys'
        assert ax.collections[0].colorbar._label == 'z'
    cm = 'cubehelix'
    ax = df.plot.scatter(x='x', y='y', c='z', colormap=cm)
    assert ax.collections[0].cmap.name == cm
    ax = df.plot.scatter(x='x', y='y', c='z', colorbar=False)
    assert ax.collections[0].colorbar is None
    ax = df.plot.scatter(x=0, y=1, c='red')
    assert ax.collections[0].colorbar is None
    self._check_colors(ax.collections, facecolors=['r'])
    df = DataFrame({'A': [1, 2], 'B': [3, 4]})
    red_rgba = [1.0, 0.0, 0.0, 1.0]
    green_rgba = [0.0, 1.0, 0.0, 1.0]
    rgba_array = np.array([red_rgba, green_rgba])
    ax = df.plot.scatter(x='A', y='B', c=rgba_array)
    tm.assert_numpy_array_equal(ax.collections[0].get_facecolor(), rgba_array)
    float_array = np.array([0.0, 1.0])
    df.plot.scatter(x='A', y='B', c=float_array, cmap='spring')