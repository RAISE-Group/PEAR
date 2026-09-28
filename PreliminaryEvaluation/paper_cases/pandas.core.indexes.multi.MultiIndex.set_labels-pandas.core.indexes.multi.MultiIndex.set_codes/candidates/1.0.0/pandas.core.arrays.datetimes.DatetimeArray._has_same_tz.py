def _has_same_tz(self, other):
    zzone = self._timezone
    if isinstance(other, np.datetime64):
        other = Timestamp(other)
    vzone = timezones.get_timezone(getattr(other, 'tzinfo', '__no_tz__'))
    return zzone == vzone