def _make_plot(self):
    x, y, c, data = (self.x, self.y, self.c, self.data)
    ax = self.axes[0]
    c_is_column = is_hashable(c) and c in self.data.columns
    cb = self.kwds.pop('colorbar', self.colormap or c_is_column)
    cmap = self.colormap or 'Greys'
    cmap = self.plt.cm.get_cmap(cmap)
    color = self.kwds.pop('color', None)
    if c is not None and color is not None:
        raise TypeError('Specify exactly one of `c` and `color`')
    elif c is None and color is None:
        c_values = self.plt.rcParams['patch.facecolor']
    elif color is not None:
        c_values = color
    elif c_is_column:
        c_values = self.data[c].values
    else:
        c_values = c
    if self.legend and hasattr(self, 'label'):
        label = self.label
    else:
        label = None
    scatter = ax.scatter(data[x].values, data[y].values, c=c_values, label=label, cmap=cmap, **self.kwds)
    if cb:
        cbar_label = c if c_is_column else ''
        self._plot_colorbar(ax, label=cbar_label)
    if label is not None:
        self._add_legend_handle(scatter, label)
    else:
        self.legend = False
    errors_x = self._get_errorbars(label=x, index=0, yerr=False)
    errors_y = self._get_errorbars(label=y, index=0, xerr=False)
    if len(errors_x) > 0 or len(errors_y) > 0:
        err_kwds = dict(errors_x, **errors_y)
        err_kwds['ecolor'] = scatter.get_facecolor()[0]
        ax.errorbar(data[x].values, data[y].values, linestyle='none', **err_kwds)