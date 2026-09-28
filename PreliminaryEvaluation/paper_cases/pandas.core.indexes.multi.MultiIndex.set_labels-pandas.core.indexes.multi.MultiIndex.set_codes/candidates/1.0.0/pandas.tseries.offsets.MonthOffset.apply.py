@apply_wraps
def apply(self, other):
    compare_day = self._get_offset_day(other)
    n = liboffsets.roll_convention(other.day, self.n, compare_day)
    return shift_month(other, n, self._day_opt)