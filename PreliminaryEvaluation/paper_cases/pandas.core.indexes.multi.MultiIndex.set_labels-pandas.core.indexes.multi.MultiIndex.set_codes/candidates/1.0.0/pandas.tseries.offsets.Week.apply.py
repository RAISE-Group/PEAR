@apply_wraps
def apply(self, other):
    if self.weekday is None:
        return other + self.n * self._inc
    if not isinstance(other, datetime):
        raise TypeError(f'Cannot add {type(other).__name__} to {type(self).__name__}')
    k = self.n
    otherDay = other.weekday()
    if otherDay != self.weekday:
        other = other + timedelta((self.weekday - otherDay) % 7)
        if k > 0:
            k -= 1
    return other + timedelta(weeks=k)