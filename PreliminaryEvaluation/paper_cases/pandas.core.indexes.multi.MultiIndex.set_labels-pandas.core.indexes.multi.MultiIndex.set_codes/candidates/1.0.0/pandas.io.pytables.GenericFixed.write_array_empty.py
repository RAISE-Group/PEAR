def write_array_empty(self, key: str, value: ArrayLike):
    """ write a 0-len array """
    arr = np.empty((1,) * value.ndim)
    self._handle.create_array(self.group, key, arr)
    node = getattr(self.group, key)
    node._v_attrs.value_type = str(value.dtype)
    node._v_attrs.shape = value.shape