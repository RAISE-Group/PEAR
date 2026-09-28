@classmethod
def _from_name(cls, suffix=None):
    if not suffix:
        raise ValueError(f'Prefix {repr(cls._prefix)} requires a suffix.')
    weekday = ccalendar.weekday_to_int[suffix]
    return cls(weekday=weekday)