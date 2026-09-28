def where(self, cond, value, other=None, subset=None, **kwargs):
    """
        Apply a function elementwise.

        Updates the HTML representation with a style which is
        selected in accordance with the return value of a function.

        .. versionadded:: 0.21.0

        Parameters
        ----------
        cond : callable
            ``cond`` should take a scalar and return a boolean.
        value : str
            Applied when ``cond`` returns true.
        other : str
            Applied when ``cond`` returns false.
        subset : IndexSlice
            A valid indexer to limit ``data`` to *before* applying the
            function. Consider using a pandas.IndexSlice.
        **kwargs : dict
            Pass along to ``cond``.

        Returns
        -------
        self : Styler

        See Also
        --------
        Styler.applymap
        """
    if other is None:
        other = ''
    return self.applymap(lambda val: value if cond(val) else other, subset=subset, **kwargs)