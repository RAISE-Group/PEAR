def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    result = ops.maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result
    raise TypeError(f'Object with dtype {self.dtype} cannot perform the numpy op {ufunc.__name__}')