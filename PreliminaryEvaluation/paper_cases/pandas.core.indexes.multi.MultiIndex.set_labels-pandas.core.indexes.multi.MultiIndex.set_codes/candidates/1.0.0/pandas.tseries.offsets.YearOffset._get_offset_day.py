def _get_offset_day(self, other):
    return liboffsets.get_day_of_month(other.replace(month=self.month), self._day_opt)