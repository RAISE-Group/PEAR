@Appender(_apply_docs['template'].format(input='dataframe', examples=_apply_docs['dataframe_examples']))
def apply(self, func, *args, **kwargs):
    func = self._is_builtin_func(func)
    if args or kwargs:
        if callable(func):

            @wraps(func)
            def f(g):
                with np.errstate(all='ignore'):
                    return func(g, *args, **kwargs)
        elif hasattr(nanops, 'nan' + func):
            f = getattr(nanops, 'nan' + func)
        else:
            raise ValueError('func must be a callable if args or kwargs are supplied')
    else:
        f = func
    with option_context('mode.chained_assignment', None):
        try:
            result = self._python_apply_general(f)
        except TypeError:
            with _group_selection_context(self):
                return self._python_apply_general(f)
    return result