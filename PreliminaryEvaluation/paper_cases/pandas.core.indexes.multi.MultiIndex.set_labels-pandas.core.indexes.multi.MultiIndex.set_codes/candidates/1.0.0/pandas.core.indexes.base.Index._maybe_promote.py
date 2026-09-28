def _maybe_promote(self, other):
    if self.inferred_type == 'date' and isinstance(other, ABCDatetimeIndex):
        return (type(other)(self), other)
    elif self.inferred_type == 'boolean':
        if not is_object_dtype(self.dtype):
            return (self.astype('object'), other.astype('object'))
    return (self, other)