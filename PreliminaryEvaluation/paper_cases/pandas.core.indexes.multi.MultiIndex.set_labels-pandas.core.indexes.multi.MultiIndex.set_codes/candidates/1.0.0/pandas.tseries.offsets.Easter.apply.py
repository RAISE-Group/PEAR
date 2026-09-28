@apply_wraps
def apply(self, other):
    current_easter = easter(other.year)
    current_easter = datetime(current_easter.year, current_easter.month, current_easter.day)
    current_easter = conversion.localize_pydatetime(current_easter, other.tzinfo)
    n = self.n
    if n >= 0 and other < current_easter:
        n -= 1
    elif n < 0 and other > current_easter:
        n += 1
    new = easter(other.year + n)
    new = datetime(new.year, new.month, new.day, other.hour, other.minute, other.second, other.microsecond)
    return new