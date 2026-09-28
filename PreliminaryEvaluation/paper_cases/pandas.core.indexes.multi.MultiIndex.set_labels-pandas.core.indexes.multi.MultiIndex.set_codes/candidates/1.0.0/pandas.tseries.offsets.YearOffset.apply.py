@apply_wraps
def apply(self, other):
    years = roll_yearday(other, self.n, self.month, self._day_opt)
    months = years * 12 + (self.month - other.month)
    return shift_month(other, months, self._day_opt)