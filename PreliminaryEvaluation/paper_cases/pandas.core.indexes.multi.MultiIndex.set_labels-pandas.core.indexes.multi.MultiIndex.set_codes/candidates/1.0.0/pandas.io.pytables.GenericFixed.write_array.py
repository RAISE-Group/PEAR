def write_array(self, key: str, value: ArrayLike, items: Optional[Index]=None):
    assert isinstance(value, (np.ndarray, ABCExtensionArray)), type(value)
    if key in self.group:
        self._handle.remove_node(self.group, key)
    empty_array = value.size == 0
    transposed = False
    if is_categorical_dtype(value):
        raise NotImplementedError('Cannot store a category dtype in a HDF5 dataset that uses format="fixed". Use format="table".')
    if not empty_array:
        if hasattr(value, 'T'):
            value = value.T
            transposed = True
    atom = None
    if self._filters is not None:
        try:
            atom = _tables().Atom.from_dtype(value.dtype)
        except ValueError:
            pass
    if atom is not None:
        if not empty_array:
            ca = self._handle.create_carray(self.group, key, atom, value.shape, filters=self._filters)
            ca[:] = value
        else:
            self.write_array_empty(key, value)
    elif value.dtype.type == np.object_:
        inferred_type = lib.infer_dtype(value.ravel(), skipna=False)
        if empty_array:
            pass
        elif inferred_type == 'string':
            pass
        else:
            ws = performance_doc % (inferred_type, key, items)
            warnings.warn(ws, PerformanceWarning, stacklevel=7)
        vlarr = self._handle.create_vlarray(self.group, key, _tables().ObjectAtom())
        vlarr.append(value)
    elif empty_array:
        self.write_array_empty(key, value)
    elif is_datetime64_dtype(value.dtype):
        self._handle.create_array(self.group, key, value.view('i8'))
        getattr(self.group, key)._v_attrs.value_type = 'datetime64'
    elif is_datetime64tz_dtype(value.dtype):
        self._handle.create_array(self.group, key, value.asi8)
        node = getattr(self.group, key)
        node._v_attrs.tz = _get_tz(value.tz)
        node._v_attrs.value_type = 'datetime64'
    elif is_timedelta64_dtype(value.dtype):
        self._handle.create_array(self.group, key, value.view('i8'))
        getattr(self.group, key)._v_attrs.value_type = 'timedelta64'
    else:
        self._handle.create_array(self.group, key, value)
    getattr(self.group, key)._v_attrs.transposed = transposed