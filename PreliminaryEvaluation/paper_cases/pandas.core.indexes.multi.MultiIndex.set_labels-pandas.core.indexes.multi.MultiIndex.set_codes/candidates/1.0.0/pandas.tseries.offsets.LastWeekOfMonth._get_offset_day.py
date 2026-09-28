def _get_offset_day(self, other):
    """
        Find the day in the same month as other that has the same
        weekday as self.weekday and is the last such day in the month.

        Parameters
        ----------
        other: datetime

        Returns
        -------
        day: int
        """
    dim = ccalendar.get_days_in_month(other.year, other.month)
    mend = datetime(other.year, other.month, dim)
    wday = mend.weekday()
    shift_days = (wday - self.weekday) % 7
    return dim - shift_days