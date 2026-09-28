def autoscale(self):
    """
        Set the view limits to include the data range.
        """
    dmin, dmax = self.datalim_to_dt()
    if dmin > dmax:
        dmax, dmin = (dmin, dmax)
    dmin, dmax = self.datalim_to_dt()
    vmin = dates.date2num(dmin)
    vmax = dates.date2num(dmax)
    return self.nonsingular(vmin, vmax)