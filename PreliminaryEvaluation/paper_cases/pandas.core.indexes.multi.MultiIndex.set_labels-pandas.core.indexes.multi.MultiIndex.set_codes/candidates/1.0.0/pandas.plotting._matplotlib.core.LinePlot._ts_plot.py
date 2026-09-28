@classmethod
def _ts_plot(cls, ax, x, data, style=None, **kwds):
    from pandas.plotting._matplotlib.timeseries import _maybe_resample, _decorate_axes, format_dateaxis
    freq, data = _maybe_resample(data, ax, kwds)
    _decorate_axes(ax, freq, kwds)
    if hasattr(ax, 'left_ax'):
        _decorate_axes(ax.left_ax, freq, kwds)
    if hasattr(ax, 'right_ax'):
        _decorate_axes(ax.right_ax, freq, kwds)
    ax._plot_data.append((data, cls._kind, kwds))
    lines = cls._plot(ax, data.index, data.values, style=style, **kwds)
    format_dateaxis(ax, ax.freq, data.index)
    return lines