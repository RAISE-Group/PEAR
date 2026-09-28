@apply_wraps
def apply(self, other):
    n = self.n
    prev_year_end, num_qtrs, tdelta = self._rollback_to_year(other)
    res = prev_year_end
    n += num_qtrs
    if self.n <= 0 and tdelta.value > 0:
        n += 1
    years = n // 4
    if years:
        res += self._offset * years
        n -= years * 4
    qtr_lens = self.get_weeks(res + Timedelta(days=1))
    weeks = sum(qtr_lens[:n])
    if weeks:
        res = liboffsets.shift_day(res, days=weeks * 7)
    return res