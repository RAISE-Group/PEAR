def _get_offset_day(self, other):
    """
        Find the day in the same month as other that has the same
        weekday as self.weekday and is the self.week'th such day in the month.

        Parameters
        ----------
        other : datetime

        Returns
        -------
        day : int
        """
    mstart = datetime(other.year, other.month, 1)
    wday = mstart.weekday()
    shift_days = (self.weekday - wday) % 7
    return 1 + shift_days + self.week * 7