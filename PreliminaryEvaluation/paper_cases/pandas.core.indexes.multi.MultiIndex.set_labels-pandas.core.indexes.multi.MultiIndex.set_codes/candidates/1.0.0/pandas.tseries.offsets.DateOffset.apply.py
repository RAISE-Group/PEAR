@apply_wraps
def apply(self, other):
    if self._use_relativedelta:
        other = as_datetime(other)
    if len(self.kwds) > 0:
        tzinfo = getattr(other, 'tzinfo', None)
        if tzinfo is not None and self._use_relativedelta:
            other = other.replace(tzinfo=None)
        if self.n > 0:
            for i in range(self.n):
                other = other + self._offset
        else:
            for i in range(-self.n):
                other = other - self._offset
        if tzinfo is not None and self._use_relativedelta:
            other = conversion.localize_pydatetime(other, tzinfo)
        return as_timestamp(other)
    else:
        return other + timedelta(self.n)