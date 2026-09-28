def __array_ufunc__(self, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any):
    cls = type(self)
    result = ops.maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result
    no_defer = (np.ndarray.__array_ufunc__, cls.__array_ufunc__)
    for item in inputs:
        higher_priority = hasattr(item, '__array_priority__') and item.__array_priority__ > self.__array_priority__
        has_array_ufunc = hasattr(item, '__array_ufunc__') and type(item).__array_ufunc__ not in no_defer and (not isinstance(item, self._HANDLED_TYPES))
        if higher_priority or has_array_ufunc:
            return NotImplemented
    names = [getattr(x, 'name') for x in inputs if hasattr(x, 'name')]
    types = tuple((type(x) for x in inputs))
    alignable = [x for x, t in zip(inputs, types) if issubclass(t, Series)]
    if len(alignable) > 1:
        index = alignable[0].index
        for s in alignable[1:]:
            index |= s.index
        inputs = tuple((x.reindex(index) if issubclass(t, Series) else x for x, t in zip(inputs, types)))
    else:
        index = self.index
    inputs = tuple((extract_array(x, extract_numpy=True) for x in inputs))
    result = getattr(ufunc, method)(*inputs, **kwargs)
    name: Optional[Hashable]
    if len(set(names)) == 1:
        name = names[0]
    else:
        name = None

    def construct_return(result):
        if lib.is_scalar(result):
            return result
        elif result.ndim > 1:
            if method == 'outer':
                raise NotImplementedError
            return result
        return self._constructor(result, index=index, name=name, copy=False)
    if type(result) is tuple:
        return tuple((construct_return(x) for x in result))
    elif method == 'at':
        return None
    else:
        return construct_return(result)