@classmethod
def _from_name(cls, suffix=None):
    kwargs = {}
    if suffix:
        kwargs['month'] = ccalendar.MONTH_TO_CAL_NUM[suffix]
    return cls(**kwargs)