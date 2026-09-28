@staticmethod
def convert(values, unit, axis):
    if is_nested_list_like(values):
        values = [DatetimeConverter._convert_1d(v, unit, axis) for v in values]
    else:
        values = DatetimeConverter._convert_1d(values, unit, axis)
    return values