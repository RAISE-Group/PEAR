@classmethod
def get_base_missing_value(cls, dtype):
    if dtype == np.int8:
        value = cls.BASE_MISSING_VALUES['int8']
    elif dtype == np.int16:
        value = cls.BASE_MISSING_VALUES['int16']
    elif dtype == np.int32:
        value = cls.BASE_MISSING_VALUES['int32']
    elif dtype == np.float32:
        value = cls.BASE_MISSING_VALUES['float32']
    elif dtype == np.float64:
        value = cls.BASE_MISSING_VALUES['float64']
    else:
        raise ValueError('Unsupported dtype')
    return value