@classmethod
def _plot(cls, ax, x, y, style=None, column_num=None, stacking_id=None, **kwds):
    if column_num == 0:
        cls._initialize_stacker(ax, stacking_id, len(y))
    y_values = cls._get_stacked_values(ax, stacking_id, y, kwds['label'])
    lines = MPLPlot._plot(ax, x, y_values, style=style, **kwds)
    cls._update_stacker(ax, stacking_id, y)
    return lines