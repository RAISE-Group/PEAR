@classmethod
@register_pandas_matplotlib_converters
def _plot(cls, ax, x, y, style=None, is_errorbar=False, **kwds):
    mask = isna(y)
    if mask.any():
        y = np.ma.array(y)
        y = np.ma.masked_where(mask, y)
    if isinstance(x, ABCIndexClass):
        x = x._mpl_repr()
    if is_errorbar:
        if 'xerr' in kwds:
            kwds['xerr'] = np.array(kwds.get('xerr'))
        if 'yerr' in kwds:
            kwds['yerr'] = np.array(kwds.get('yerr'))
        return ax.errorbar(x, y, **kwds)
    else:
        if style is not None:
            args = (x, y, style)
        else:
            args = (x, y)
        return ax.plot(*args, **kwds)