@classmethod
def _from_name(cls, suffix=None):
    if not suffix:
        weekday = None
    else:
        weekday = ccalendar.weekday_to_int[suffix]
    return cls(weekday=weekday)