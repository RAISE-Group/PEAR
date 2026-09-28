def autoscale(self):
    """
        Sets the view limits to the nearest multiples of base that contain the
        data.
        """
    vmin, vmax = self.axis.get_data_interval()
    locs = self._get_default_locs(vmin, vmax)
    vmin, vmax = locs[[0, -1]]
    if vmin == vmax:
        vmin -= 1
        vmax += 1
    return nonsingular(vmin, vmax)