@cache_readonly
def next_bday(self):
    """
        Used for moving to next business day.
        """
    if self.n >= 0:
        nb_offset = 1
    else:
        nb_offset = -1
    if self._prefix.startswith('C'):
        return CustomBusinessDay(n=nb_offset, weekmask=self.weekmask, holidays=self.holidays, calendar=self.calendar)
    else:
        return BusinessDay(n=nb_offset)