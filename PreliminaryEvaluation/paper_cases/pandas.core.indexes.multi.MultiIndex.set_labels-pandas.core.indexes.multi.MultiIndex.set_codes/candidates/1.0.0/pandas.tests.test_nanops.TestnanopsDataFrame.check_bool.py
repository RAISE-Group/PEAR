def check_bool(self, func, value, correct):
    while getattr(value, 'ndim', True):
        res0 = func(value)
        if correct:
            assert res0
        else:
            assert not res0
        if not hasattr(value, 'ndim'):
            break
        value = np.take(value, 0, axis=-1)