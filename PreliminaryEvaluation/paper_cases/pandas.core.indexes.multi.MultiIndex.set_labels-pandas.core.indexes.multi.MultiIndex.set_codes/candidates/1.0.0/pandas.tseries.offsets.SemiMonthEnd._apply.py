def _apply(self, n, other):
    months = n // 2
    day = 31 if n % 2 else self.day_of_month
    return shift_month(other, months, day)