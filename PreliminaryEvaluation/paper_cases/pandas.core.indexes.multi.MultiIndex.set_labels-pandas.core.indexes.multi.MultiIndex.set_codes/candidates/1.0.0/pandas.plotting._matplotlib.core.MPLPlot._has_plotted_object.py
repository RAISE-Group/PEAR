def _has_plotted_object(self, ax):
    """check whether ax has data"""
    return len(ax.lines) != 0 or len(ax.artists) != 0 or len(ax.containers) != 0