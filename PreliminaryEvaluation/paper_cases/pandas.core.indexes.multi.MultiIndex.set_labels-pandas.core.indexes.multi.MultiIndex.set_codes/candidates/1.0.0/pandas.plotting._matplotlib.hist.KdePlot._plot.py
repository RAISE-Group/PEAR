@classmethod
def _plot(cls, ax, y, style=None, bw_method=None, ind=None, column_num=None, stacking_id=None, **kwds):
    from scipy.stats import gaussian_kde
    y = remove_na_arraylike(y)
    gkde = gaussian_kde(y, bw_method=bw_method)
    y = gkde.evaluate(ind)
    lines = MPLPlot._plot(ax, ind, y, style=style, **kwds)
    return lines