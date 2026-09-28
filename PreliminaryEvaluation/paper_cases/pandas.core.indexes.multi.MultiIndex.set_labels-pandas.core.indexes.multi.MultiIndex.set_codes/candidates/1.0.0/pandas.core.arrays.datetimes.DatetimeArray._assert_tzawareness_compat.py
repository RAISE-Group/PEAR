def _assert_tzawareness_compat(self, other):
    other_tz = getattr(other, 'tzinfo', None)
    if is_datetime64tz_dtype(other):
        other_tz = other.dtype.tz
    if other is NaT:
        pass
    elif self.tz is None:
        if other_tz is not None:
            raise TypeError('Cannot compare tz-naive and tz-aware datetime-like objects.')
    elif other_tz is None:
        raise TypeError('Cannot compare tz-naive and tz-aware datetime-like objects')