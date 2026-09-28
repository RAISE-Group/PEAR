def test_scatter_colors(self):
    df = DataFrame({'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]})
    with pytest.raises(TypeError):
        df.plot.scatter(x='a', y='b', c='c', color='green')
    default_colors = self._unpack_cycler(self.plt.rcParams)
    ax = df.plot.scatter(x='a', y='b', c='c')
    tm.assert_numpy_array_equal(ax.collections[0].get_facecolor()[0], np.array(self.colorconverter.to_rgba(default_colors[0])))
    ax = df.plot.scatter(x='a', y='b', color='white')
    tm.assert_numpy_array_equal(ax.collections[0].get_facecolor()[0], np.array([1, 1, 1, 1], dtype=np.float64))