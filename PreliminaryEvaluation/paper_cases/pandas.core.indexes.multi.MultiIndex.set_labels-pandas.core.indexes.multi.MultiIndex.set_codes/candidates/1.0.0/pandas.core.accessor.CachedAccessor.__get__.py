def __get__(self, obj, cls):
    if obj is None:
        return self._accessor
    accessor_obj = self._accessor(obj)
    object.__setattr__(obj, self._name, accessor_obj)
    return accessor_obj