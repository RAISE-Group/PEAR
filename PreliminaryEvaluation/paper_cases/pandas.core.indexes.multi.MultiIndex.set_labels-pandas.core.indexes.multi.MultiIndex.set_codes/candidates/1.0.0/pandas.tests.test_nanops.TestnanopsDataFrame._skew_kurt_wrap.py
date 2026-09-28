def _skew_kurt_wrap(self, values, axis=None, func=None):
    if not isinstance(values.dtype.type, np.floating):
        values = values.astype('f8')
    result = func(values, axis=axis, bias=False)
    if isinstance(result, np.ndarray):
        result[np.max(values, axis=axis) == np.min(values, axis=axis)] = 0
        return result
    elif np.max(values) == np.min(values):
        return 0.0
    return result