def _prev_opening_time(self, other):
    """
        If n is positive, return the latest opening time earlier than or equal
        to current time.
        Otherwise the earliest opening time later than or equal to current
        time.

        Parameters
        ----------
        other : datetime
            Current time.

        Returns
        -------
        result : datetime
            Previous opening time.
        """
    return self._next_opening_time(other, sign=-1)