@pytest.mark.xfail
def test_plot_accessor_updates_on_inplace(self):
    s = Series([1, 2, 3, 4])
    _, ax = self.plt.subplots()
    ax = s.plot(ax=ax)
    before = ax.xaxis.get_ticklocs()
    s.drop([0, 1], inplace=True)
    _, ax = self.plt.subplots()
    after = ax.xaxis.get_ticklocs()
    tm.assert_numpy_array_equal(before, after)