@apply_wraps
def apply(self, other):
    norm = Timestamp(other).normalize()
    n = self.n
    prev_year = self.get_year_end(datetime(other.year - 1, self.startingMonth, 1))
    cur_year = self.get_year_end(datetime(other.year, self.startingMonth, 1))
    next_year = self.get_year_end(datetime(other.year + 1, self.startingMonth, 1))
    prev_year = conversion.localize_pydatetime(prev_year, other.tzinfo)
    cur_year = conversion.localize_pydatetime(cur_year, other.tzinfo)
    next_year = conversion.localize_pydatetime(next_year, other.tzinfo)
    if norm == prev_year:
        n -= 1
    elif norm == cur_year:
        pass
    elif n > 0:
        if norm < prev_year:
            n -= 2
        elif prev_year < norm < cur_year:
            n -= 1
        elif cur_year < norm < next_year:
            pass
    elif cur_year < norm < next_year:
        n += 1
    elif prev_year < norm < cur_year:
        pass
    elif norm.year == prev_year.year and norm < prev_year and (prev_year - norm <= timedelta(6)):
        n -= 1
    else:
        assert False
    shifted = datetime(other.year + n, self.startingMonth, 1)
    result = self.get_year_end(shifted)
    result = datetime(result.year, result.month, result.day, other.hour, other.minute, other.second, other.microsecond)
    return result