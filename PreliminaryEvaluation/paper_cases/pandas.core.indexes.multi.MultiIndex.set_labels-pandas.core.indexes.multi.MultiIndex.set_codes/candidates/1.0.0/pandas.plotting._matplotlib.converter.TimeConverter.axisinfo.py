@staticmethod
def axisinfo(unit, axis):
    if unit != 'time':
        return None
    majloc = AutoLocator()
    majfmt = TimeFormatter(majloc)
    return units.AxisInfo(majloc=majloc, majfmt=majfmt, label='time')