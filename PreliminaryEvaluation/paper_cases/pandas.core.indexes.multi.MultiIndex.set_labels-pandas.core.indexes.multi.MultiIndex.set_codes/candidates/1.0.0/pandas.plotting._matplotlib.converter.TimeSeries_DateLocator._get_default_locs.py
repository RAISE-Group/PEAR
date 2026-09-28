def _get_default_locs(self, vmin, vmax):
    """Returns the default locations of ticks."""
    if self.plot_obj.date_axis_info is None:
        self.plot_obj.date_axis_info = self.finder(vmin, vmax, self.freq)
    locator = self.plot_obj.date_axis_info
    if self.isminor:
        return np.compress(locator['min'], locator['val'])
    return np.compress(locator['maj'], locator['val'])