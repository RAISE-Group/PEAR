def _values_for_factorize(self):
    frozen = self._values_for_argsort()
    if len(frozen) == 0:
        frozen = frozen.ravel()
    return (frozen, ())