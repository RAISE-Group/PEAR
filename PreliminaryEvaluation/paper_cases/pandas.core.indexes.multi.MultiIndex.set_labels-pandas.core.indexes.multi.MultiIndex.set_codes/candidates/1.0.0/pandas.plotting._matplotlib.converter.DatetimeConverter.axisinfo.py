@staticmethod
def axisinfo(unit, axis):
    """
        Return the :class:`~matplotlib.units.AxisInfo` for *unit*.

        *unit* is a tzinfo instance or None.
        The *axis* argument is required but not used.
        """
    tz = unit
    majloc = PandasAutoDateLocator(tz=tz)
    majfmt = PandasAutoDateFormatter(majloc, tz=tz)
    datemin = pydt.date(2000, 1, 1)
    datemax = pydt.date(2010, 1, 1)
    return units.AxisInfo(majloc=majloc, majfmt=majfmt, label='', default_limits=(datemin, datemax))