@classmethod
def _add_logical_methods(cls):
    """
        Add in logical methods.
        """
    _doc = '\n        %(desc)s\n\n        Parameters\n        ----------\n        *args\n            These parameters will be passed to numpy.%(outname)s.\n        **kwargs\n            These parameters will be passed to numpy.%(outname)s.\n\n        Returns\n        -------\n        %(outname)s : bool or array_like (if axis is specified)\n            A single element array_like may be converted to bool.'
    _index_shared_docs['index_all'] = dedent('\n\n        See Also\n        --------\n        Index.any : Return whether any element in an Index is True.\n        Series.any : Return whether any element in a Series is True.\n        Series.all : Return whether all elements in a Series are True.\n\n        Notes\n        -----\n        Not a Number (NaN), positive infinity and negative infinity\n        evaluate to True because these are not equal to zero.\n\n        Examples\n        --------\n        **all**\n\n        True, because nonzero integers are considered True.\n\n        >>> pd.Index([1, 2, 3]).all()\n        True\n\n        False, because ``0`` is considered False.\n\n        >>> pd.Index([0, 1, 2]).all()\n        False\n\n        **any**\n\n        True, because ``1`` is considered True.\n\n        >>> pd.Index([0, 0, 1]).any()\n        True\n\n        False, because ``0`` is considered False.\n\n        >>> pd.Index([0, 0, 0]).any()\n        False\n        ')
    _index_shared_docs['index_any'] = dedent('\n\n        See Also\n        --------\n        Index.all : Return whether all elements are True.\n        Series.all : Return whether all elements are True.\n\n        Notes\n        -----\n        Not a Number (NaN), positive infinity and negative infinity\n        evaluate to True because these are not equal to zero.\n\n        Examples\n        --------\n        >>> index = pd.Index([0, 1, 2])\n        >>> index.any()\n        True\n\n        >>> index = pd.Index([0, 0, 0])\n        >>> index.any()\n        False\n        ')

    def _make_logical_function(name, desc, f):

        @Substitution(outname=name, desc=desc)
        @Appender(_index_shared_docs['index_' + name])
        @Appender(_doc)
        def logical_func(self, *args, **kwargs):
            result = f(self.values)
            if isinstance(result, (np.ndarray, ABCSeries, Index)) and result.ndim == 0:
                return result.dtype.type(result.item())
            else:
                return result
        logical_func.__name__ = name
        return logical_func
    cls.all = _make_logical_function('all', 'Return whether all elements are True.', np.all)
    cls.any = _make_logical_function('any', 'Return whether any element is True.', np.any)