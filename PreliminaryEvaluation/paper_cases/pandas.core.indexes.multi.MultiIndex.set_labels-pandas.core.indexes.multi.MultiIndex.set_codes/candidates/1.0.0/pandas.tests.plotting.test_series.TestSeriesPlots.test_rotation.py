def test_rotation(self):
    df = DataFrame(randn(5, 5))
    _, ax = self.plt.subplots()
    axes = df.plot(ax=ax)
    self._check_ticks_props(axes, xrot=0)
    _, ax = self.plt.subplots()
    axes = df.plot(rot=30, ax=ax)
    self._check_ticks_props(axes, xrot=30)