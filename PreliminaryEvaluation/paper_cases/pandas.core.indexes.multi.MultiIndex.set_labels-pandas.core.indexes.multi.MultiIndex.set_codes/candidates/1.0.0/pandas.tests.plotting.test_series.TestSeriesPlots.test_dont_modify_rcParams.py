def test_dont_modify_rcParams(self):
    key = 'axes.prop_cycle'
    colors = self.plt.rcParams[key]
    _, ax = self.plt.subplots()
    Series([1, 2, 3]).plot(ax=ax)
    assert colors == self.plt.rcParams[key]