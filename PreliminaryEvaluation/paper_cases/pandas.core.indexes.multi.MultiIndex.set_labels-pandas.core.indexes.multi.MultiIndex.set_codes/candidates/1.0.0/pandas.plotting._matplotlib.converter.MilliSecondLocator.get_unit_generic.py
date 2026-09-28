@staticmethod
def get_unit_generic(freq):
    unit = dates.RRuleLocator.get_unit_generic(freq)
    if unit < 0:
        return MilliSecondLocator.UNIT
    return unit