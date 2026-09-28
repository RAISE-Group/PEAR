def _make_wrapper(self, name):
    assert name in self._apply_whitelist
    self._set_group_selection()
    f = getattr(self._selected_obj, name)
    if not isinstance(f, types.MethodType):
        return self.apply(lambda self: getattr(self, name))
    f = getattr(type(self._selected_obj), name)
    sig = inspect.signature(f)

    def wrapper(*args, **kwargs):
        if 'axis' in sig.parameters:
            if kwargs.get('axis', None) is None:
                kwargs['axis'] = self.axis

        def curried(x):
            return f(x, *args, **kwargs)
        curried.__name__ = name
        if name in base.plotting_methods:
            return self.apply(curried)
        try:
            return self.apply(curried)
        except TypeError as err:
            if not re.search("reduction operation '.*' not allowed for this dtype", str(err)):
                raise
        if self.obj.ndim == 1:
            raise ValueError
        result = self._aggregate_item_by_item(name, *args, **kwargs)
        return result
    wrapper.__name__ = name
    return wrapper