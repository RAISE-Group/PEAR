@classmethod
def _from_name(cls, suffix=None):
    if not suffix:
        raise ValueError(f'Prefix {repr(cls._prefix)} requires a suffix.')
    week = int(suffix[0]) - 1
    weekday = ccalendar.weekday_to_int[suffix[1:]]
    return cls(week=week, weekday=weekday)