@staticmethod
def convert(value, unit, axis):
    valid_types = (str, pydt.time)
    if isinstance(value, valid_types) or is_integer(value) or is_float(value):
        return time2num(value)
    if isinstance(value, Index):
        return value.map(time2num)
    if isinstance(value, (list, tuple, np.ndarray, Index)):
        return [time2num(x) for x in value]
    return value