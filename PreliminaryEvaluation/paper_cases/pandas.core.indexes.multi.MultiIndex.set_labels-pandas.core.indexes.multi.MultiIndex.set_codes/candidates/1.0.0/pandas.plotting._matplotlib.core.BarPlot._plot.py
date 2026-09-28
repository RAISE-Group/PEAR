@classmethod
def _plot(cls, ax, x, y, w, start=0, log=False, **kwds):
    return ax.bar(x, y, w, bottom=start, log=log, **kwds)