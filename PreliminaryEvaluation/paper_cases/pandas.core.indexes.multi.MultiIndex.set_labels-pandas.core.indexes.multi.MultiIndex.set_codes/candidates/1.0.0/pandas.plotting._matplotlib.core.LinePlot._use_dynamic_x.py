def _use_dynamic_x(self):
    from pandas.plotting._matplotlib.timeseries import _use_dynamic_x
    return _use_dynamic_x(self._get_ax(0), self.data)