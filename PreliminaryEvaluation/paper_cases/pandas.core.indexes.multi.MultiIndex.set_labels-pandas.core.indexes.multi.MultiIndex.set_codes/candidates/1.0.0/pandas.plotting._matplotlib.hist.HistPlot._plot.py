@classmethod
def _plot(cls, ax, y, style=None, bins=None, bottom=0, column_num=0, stacking_id=None, **kwds):
    if column_num == 0:
        cls._initialize_stacker(ax, stacking_id, len(bins) - 1)
    y = y[~isna(y)]
    base = np.zeros(len(bins) - 1)
    bottom = bottom + cls._get_stacked_values(ax, stacking_id, base, kwds['label'])
    n, bins, patches = ax.hist(y, bins=bins, bottom=bottom, **kwds)
    cls._update_stacker(ax, stacking_id, n)
    return patches