def _next_opening_time(self, other, sign=1):
    """
        If self.n and sign have the same sign, return the earliest opening time
        later than or equal to current time.
        Otherwise the latest opening time earlier than or equal to current
        time.

        Opening time always locates on BusinessDay.
        However, closing time may not if business hour extends over midnight.

        Parameters
        ----------
        other : datetime
            Current time.
        sign : int, default 1.
            Either 1 or -1. Going forward in time if it has the same sign as
            self.n. Going backward in time otherwise.

        Returns
        -------
        result : datetime
            Next opening time.
        """
    earliest_start = self.start[0]
    latest_start = self.start[-1]
    if not self.next_bday.is_on_offset(other):
        other = other + sign * self.next_bday
        if self.n * sign >= 0:
            hour, minute = (earliest_start.hour, earliest_start.minute)
        else:
            hour, minute = (latest_start.hour, latest_start.minute)
    elif self.n * sign >= 0:
        if latest_start < other.time():
            other = other + sign * self.next_bday
            hour, minute = (earliest_start.hour, earliest_start.minute)
        else:
            for st in self.start:
                if other.time() <= st:
                    hour, minute = (st.hour, st.minute)
                    break
    elif other.time() < earliest_start:
        other = other + sign * self.next_bday
        hour, minute = (latest_start.hour, latest_start.minute)
    else:
        for st in reversed(self.start):
            if other.time() >= st:
                hour, minute = (st.hour, st.minute)
                break
    return datetime(other.year, other.month, other.day, hour, minute)