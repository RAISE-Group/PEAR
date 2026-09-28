def format(self, formatter, subset=None, na_rep: Optional[str]=None):
    """
        Format the text display value of cells.

        Parameters
        ----------
        formatter : str, callable, dict or None
            If ``formatter`` is None, the default formatter is used
        subset : IndexSlice
            An argument to ``DataFrame.loc`` that restricts which elements
            ``formatter`` is applied to.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied

            .. versionadded:: 1.0.0

        Returns
        -------
        self : Styler

        Notes
        -----

        ``formatter`` is either an ``a`` or a dict ``{column name: a}`` where
        ``a`` is one of

        - str: this will be wrapped in: ``a.format(x)``
        - callable: called with the value of an individual cell

        The default display value for numeric values is the "general" (``g``)
        format with ``pd.options.display.precision`` precision.

        Examples
        --------

        >>> df = pd.DataFrame(np.random.randn(4, 2), columns=['a', 'b'])
        >>> df.style.format("{:.2%}")
        >>> df['c'] = ['a', 'b', 'c', 'd']
        >>> df.style.format({'c': str.upper})
        """
    if formatter is None:
        assert self._display_funcs.default_factory is not None
        formatter = self._display_funcs.default_factory()
    if subset is None:
        row_locs = range(len(self.data))
        col_locs = range(len(self.data.columns))
    else:
        subset = _non_reducing_slice(subset)
        if len(subset) == 1:
            subset = (subset, self.data.columns)
        sub_df = self.data.loc[subset]
        row_locs = self.data.index.get_indexer_for(sub_df.index)
        col_locs = self.data.columns.get_indexer_for(sub_df.columns)
    if is_dict_like(formatter):
        for col, col_formatter in formatter.items():
            col_formatter = _maybe_wrap_formatter(col_formatter, na_rep)
            col_num = self.data.columns.get_indexer_for([col])[0]
            for row_num in row_locs:
                self._display_funcs[row_num, col_num] = col_formatter
    else:
        formatter = _maybe_wrap_formatter(formatter, na_rep)
        locs = product(*(row_locs, col_locs))
        for i, j in locs:
            self._display_funcs[i, j] = formatter
    return self