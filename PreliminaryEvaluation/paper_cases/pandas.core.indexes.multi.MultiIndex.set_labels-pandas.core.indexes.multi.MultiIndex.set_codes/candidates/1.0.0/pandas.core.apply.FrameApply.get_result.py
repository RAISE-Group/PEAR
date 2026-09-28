def get_result(self):
    """ compute the results """
    if is_list_like(self.f) or is_dict_like(self.f):
        return self.obj.aggregate(self.f, *self.args, axis=self.axis, **self.kwds)
    if len(self.columns) == 0 and len(self.index) == 0:
        return self.apply_empty_result()
    if isinstance(self.f, str):
        func = getattr(self.obj, self.f)
        sig = inspect.getfullargspec(func)
        if 'axis' in sig.args:
            self.kwds['axis'] = self.axis
        return func(*self.args, **self.kwds)
    elif isinstance(self.f, np.ufunc):
        with np.errstate(all='ignore'):
            results = self.obj._data.apply('apply', func=self.f)
        return self.obj._constructor(data=results, index=self.index, columns=self.columns, copy=False)
    if self.result_type == 'broadcast':
        return self.apply_broadcast(self.obj)
    elif not all(self.obj.shape):
        return self.apply_empty_result()
    elif self.raw and (not self.obj._is_mixed_type):
        return self.apply_raw()
    return self.apply_standard()