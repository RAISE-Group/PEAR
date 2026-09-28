@staticmethod
def convert(values, units, axis):
    if is_nested_list_like(values):
        values = [PeriodConverter._convert_1d(v, units, axis) for v in values]
    else:
        values = PeriodConverter._convert_1d(values, units, axis)
    return values