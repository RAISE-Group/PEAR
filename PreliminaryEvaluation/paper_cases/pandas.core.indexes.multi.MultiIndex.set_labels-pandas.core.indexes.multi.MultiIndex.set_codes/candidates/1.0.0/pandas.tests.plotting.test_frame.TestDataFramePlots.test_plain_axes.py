def test_plain_axes(self):
    fig, ax = self.plt.subplots()
    fig.add_axes([0.2, 0.2, 0.2, 0.2])
    Series(rand(10)).plot(ax=ax)
    df = DataFrame({'a': randn(8), 'b': randn(8)})
    fig = self.plt.figure()
    ax = fig.add_axes((0, 0, 1, 1))
    df.plot(kind='scatter', ax=ax, x='a', y='b', c='a', cmap='hsv')
    fig, ax = self.plt.subplots()
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    Series(rand(10)).plot(ax=ax)
    Series(rand(10)).plot(ax=cax)
    fig, ax = self.plt.subplots()
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    iax = inset_axes(ax, width='30%', height=1.0, loc=3)
    Series(rand(10)).plot(ax=ax)
    Series(rand(10)).plot(ax=iax)