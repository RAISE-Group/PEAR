def _make_plot_keywords(self, kwds, y):
    kwds['bw_method'] = self.bw_method
    kwds['ind'] = self._get_ind(y)
    return kwds