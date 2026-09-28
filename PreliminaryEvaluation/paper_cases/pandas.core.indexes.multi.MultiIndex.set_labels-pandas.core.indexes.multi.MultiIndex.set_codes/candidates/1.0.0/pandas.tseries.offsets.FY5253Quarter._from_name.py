@classmethod
def _from_name(cls, *args):
    return cls(**dict(FY5253._parse_suffix(*args[:-1]), qtr_with_extra_week=int(args[-1])))