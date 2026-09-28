@apply_wraps
def apply(self, other):
    n = liboffsets.roll_convention(other.day, self.n, self.day_of_month)
    days_in_month = ccalendar.get_days_in_month(other.year, other.month)
    if type(self) is SemiMonthBegin and (self.n <= 0 and other.day == 1):
        n -= 1
    elif type(self) is SemiMonthEnd and (self.n > 0 and other.day == days_in_month):
        n += 1
    return self._apply(n, other)