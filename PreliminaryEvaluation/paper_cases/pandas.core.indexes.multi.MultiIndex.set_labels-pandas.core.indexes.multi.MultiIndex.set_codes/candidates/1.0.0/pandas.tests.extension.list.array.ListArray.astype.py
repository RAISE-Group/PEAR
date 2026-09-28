def astype(self, dtype, copy=True):
    if isinstance(dtype, type(self.dtype)) and dtype == self.dtype:
        if copy:
            return self.copy()
        return self
    elif pd.api.types.is_string_dtype(dtype) and (not pd.api.types.is_object_dtype(dtype)):
        return np.array([str(x) for x in self.data], dtype=dtype)
    return np.array(self.data, dtype=dtype, copy=copy)