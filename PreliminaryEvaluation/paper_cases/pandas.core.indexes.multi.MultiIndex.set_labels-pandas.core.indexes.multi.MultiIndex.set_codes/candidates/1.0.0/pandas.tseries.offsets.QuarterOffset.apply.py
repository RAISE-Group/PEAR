@apply_wraps
def apply(self, other):
    months_since = other.month % 3 - self.startingMonth % 3
    qtrs = liboffsets.roll_qtrday(other, self.n, self.startingMonth, day_opt=self._day_opt, modby=3)
    months = qtrs * 3 - months_since
    return shift_month(other, months, self._day_opt)