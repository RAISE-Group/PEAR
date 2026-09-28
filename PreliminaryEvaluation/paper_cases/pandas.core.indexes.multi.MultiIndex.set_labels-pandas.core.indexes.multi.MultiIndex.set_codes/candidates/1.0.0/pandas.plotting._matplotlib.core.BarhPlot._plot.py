@classmethod
def _plot(cls, ax, x, y, w, start=0, log=False, **kwds):
    return ax.barh(x, y, w, left=start, log=log, **kwds)