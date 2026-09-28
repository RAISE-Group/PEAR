@classmethod
def _plot(cls, ax, y, column_num=None, return_type='axes', **kwds):
    if y.ndim == 2:
        y = [remove_na_arraylike(v) for v in y]
        y = [v if v.size > 0 else np.array([np.nan]) for v in y]
    else:
        y = remove_na_arraylike(y)
    bp = ax.boxplot(y, **kwds)
    if return_type == 'dict':
        return (bp, bp)
    elif return_type == 'both':
        return (cls.BP(ax=ax, lines=bp), bp)
    else:
        return (ax, bp)