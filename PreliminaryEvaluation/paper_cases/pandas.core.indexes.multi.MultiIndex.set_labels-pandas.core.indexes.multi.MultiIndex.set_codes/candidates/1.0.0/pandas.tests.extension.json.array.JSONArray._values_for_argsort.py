def _values_for_argsort(self):
    frozen = [()] + [tuple(x.items()) for x in self]
    return np.array(frozen, dtype=object)[1:]