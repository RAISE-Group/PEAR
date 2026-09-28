def _construct_axes_from_arguments(self, args, kwargs, require_all: bool=False, sentinel=None):
    """Construct and returns axes if supplied in args/kwargs.

        If require_all, raise if all axis arguments are not supplied
        return a tuple of (axes, kwargs).

        sentinel specifies the default parameter when an axis is not
        supplied; useful to distinguish when a user explicitly passes None
        in scenarios where None has special meaning.
        """
    args = list(args)
    for a in self._AXIS_ORDERS:
        if a not in kwargs:
            try:
                kwargs[a] = args.pop(0)
            except IndexError:
                if require_all:
                    raise TypeError('not enough/duplicate arguments specified!')
    axes = {a: kwargs.pop(a, sentinel) for a in self._AXIS_ORDERS}
    return (axes, kwargs)