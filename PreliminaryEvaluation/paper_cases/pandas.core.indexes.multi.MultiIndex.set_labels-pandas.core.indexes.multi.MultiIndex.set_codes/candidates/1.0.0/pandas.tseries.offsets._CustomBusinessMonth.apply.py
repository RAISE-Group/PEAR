@apply_wraps
def apply(self, other):
    cur_month_offset_date = self.month_roll(other)
    compare_date = self.cbday_roll(cur_month_offset_date)
    n = liboffsets.roll_convention(other.day, self.n, compare_date.day)
    new = cur_month_offset_date + n * self.m_offset
    result = self.cbday_roll(new)
    return result