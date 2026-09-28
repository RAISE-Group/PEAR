def _plot_colorbar(self, ax, **kwds):
    img = ax.collections[0]
    cbar = self.fig.colorbar(img, ax=ax, **kwds)
    if _mpl_ge_3_0_0():
        return
    points = ax.get_position().get_points()
    cbar_points = cbar.ax.get_position().get_points()
    cbar.ax.set_position([cbar_points[0, 0], points[0, 1], cbar_points[1, 0] - cbar_points[0, 0], points[1, 1] - points[0, 1]])