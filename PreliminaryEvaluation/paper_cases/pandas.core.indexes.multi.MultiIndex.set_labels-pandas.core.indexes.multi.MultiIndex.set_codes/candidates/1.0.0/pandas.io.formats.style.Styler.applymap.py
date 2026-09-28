def applymap(self, func, subset=None, **kwargs):
    """
        Apply a function elementwise.

        Updates the HTML representation with the result.

        Parameters
        ----------
        func : function
            ``func`` should take a scalar and return a scalar.
        subset : IndexSlice
            A valid indexer to limit ``data`` to *before* applying the
            function. Consider using a pandas.IndexSlice.
        **kwargs : dict
            Pass along to ``func``.

        Returns
        -------
        self : Styler

        See Also
        --------
        Styler.where
        """
    self._todo.append((lambda instance: getattr(instance, '_applymap'), (func, subset), kwargs))
    return self