@classmethod
def _from_name(cls, suffix=None):
    kwargs = {}
    if suffix:
        kwargs['startingMonth'] = ccalendar.MONTH_TO_CAL_NUM[suffix]
    elif cls._from_name_startingMonth is not None:
        kwargs['startingMonth'] = cls._from_name_startingMonth
    return cls(**kwargs)