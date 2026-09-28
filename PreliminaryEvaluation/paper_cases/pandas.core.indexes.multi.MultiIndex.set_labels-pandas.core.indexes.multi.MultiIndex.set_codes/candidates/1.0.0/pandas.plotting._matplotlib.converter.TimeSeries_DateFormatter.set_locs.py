def set_locs(self, locs):
    """Sets the locations of the ticks"""
    self.locs = locs
    vmin, vmax = vi = tuple(self.axis.get_view_interval())
    if vi != self.plot_obj.view_interval:
        self.plot_obj.date_axis_info = None
    self.plot_obj.view_interval = vi
    if vmax < vmin:
        vmin, vmax = (vmax, vmin)
    self._set_default_format(vmin, vmax)