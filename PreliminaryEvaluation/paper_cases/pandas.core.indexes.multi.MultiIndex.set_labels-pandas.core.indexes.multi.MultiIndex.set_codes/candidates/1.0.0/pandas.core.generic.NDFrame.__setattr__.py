def __setattr__(self, name: str, value) -> None:
    """After regular attribute access, try setting the name
        This allows simpler access to columns for interactive use.
        """
    try:
        object.__getattribute__(self, name)
        return object.__setattr__(self, name, value)
    except AttributeError:
        pass
    if name in self._internal_names_set:
        object.__setattr__(self, name, value)
    elif name in self._metadata:
        object.__setattr__(self, name, value)
    else:
        try:
            existing = getattr(self, name)
            if isinstance(existing, Index):
                object.__setattr__(self, name, value)
            elif name in self._info_axis:
                self[name] = value
            else:
                object.__setattr__(self, name, value)
        except (AttributeError, TypeError):
            if isinstance(self, ABCDataFrame) and is_list_like(value):
                warnings.warn("Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access", stacklevel=2)
            object.__setattr__(self, name, value)