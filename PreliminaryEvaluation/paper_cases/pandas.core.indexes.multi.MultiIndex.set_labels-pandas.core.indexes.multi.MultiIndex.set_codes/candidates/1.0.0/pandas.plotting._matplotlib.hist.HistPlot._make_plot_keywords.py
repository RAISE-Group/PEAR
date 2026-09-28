def _make_plot_keywords(self, kwds, y):
    """merge BoxPlot/KdePlot properties to passed kwds"""
    kwds['bottom'] = self.bottom
    kwds['bins'] = self.bins
    return kwds