def _is_ts_plot(self):
    return not self.x_compat and self.use_index and self._use_dynamic_x()