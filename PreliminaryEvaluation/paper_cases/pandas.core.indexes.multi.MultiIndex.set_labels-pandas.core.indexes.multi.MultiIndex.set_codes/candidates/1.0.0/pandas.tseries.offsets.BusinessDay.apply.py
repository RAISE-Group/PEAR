@apply_wraps
def apply(self, other):
    if isinstance(other, datetime):
        n = self.n
        wday = other.weekday()
        weeks = n // 5
        if n <= 0 and wday > 4:
            n += 1
        n -= 5 * weeks
        if n == 0 and wday > 4:
            days = 4 - wday
        elif wday > 4:
            days = 7 - wday + (n - 1)
        elif wday + n <= 4:
            days = n
        else:
            days = n + 2
        result = other + timedelta(days=7 * weeks + days)
        if self.offset:
            result = result + self.offset
        return result
    elif isinstance(other, (timedelta, Tick)):
        return BDay(self.n, offset=self.offset + other, normalize=self.normalize)
    else:
        raise ApplyTypeError('Only know how to combine business day with datetime or timedelta.')