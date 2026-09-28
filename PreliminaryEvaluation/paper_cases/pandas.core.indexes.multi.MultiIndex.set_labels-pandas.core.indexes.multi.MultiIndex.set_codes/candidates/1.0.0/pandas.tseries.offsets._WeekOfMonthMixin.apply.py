@apply_wraps
def apply(self, other):
    compare_day = self._get_offset_day(other)
    months = self.n
    if months > 0 and compare_day > other.day:
        months -= 1
    elif months <= 0 and compare_day < other.day:
        months += 1
    shifted = shift_month(other, months, 'start')
    to_day = self._get_offset_day(shifted)
    return liboffsets.shift_day(shifted, to_day - shifted.day)