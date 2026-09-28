def _get_binner_for_time(self):
    if self.kind == 'period':
        return self.groupby._get_time_period_bins(self.ax)
    return self.groupby._get_time_bins(self.ax)