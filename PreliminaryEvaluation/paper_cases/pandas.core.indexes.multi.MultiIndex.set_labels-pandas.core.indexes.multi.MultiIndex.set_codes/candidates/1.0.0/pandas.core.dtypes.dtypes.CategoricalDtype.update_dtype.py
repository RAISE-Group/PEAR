def update_dtype(self, dtype: Union[str_type, 'CategoricalDtype']) -> 'CategoricalDtype':
    """
        Returns a CategoricalDtype with categories and ordered taken from dtype
        if specified, otherwise falling back to self if unspecified

        Parameters
        ----------
        dtype : CategoricalDtype

        Returns
        -------
        new_dtype : CategoricalDtype
        """
    if isinstance(dtype, str) and dtype == 'category':
        return self
    elif not self.is_dtype(dtype):
        raise ValueError(f'a CategoricalDtype must be passed to perform an update, got {repr(dtype)}')
    else:
        dtype = cast(CategoricalDtype, dtype)
    new_categories = dtype.categories if dtype.categories is not None else self.categories
    new_ordered = dtype.ordered if dtype.ordered is not None else self.ordered
    return CategoricalDtype(new_categories, new_ordered)