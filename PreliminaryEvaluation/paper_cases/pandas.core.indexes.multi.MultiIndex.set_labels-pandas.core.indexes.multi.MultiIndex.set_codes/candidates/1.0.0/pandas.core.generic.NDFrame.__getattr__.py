def __getattr__(self, name: str):
    """After regular attribute access, try looking up the name
        This allows simpler access to columns for interactive use.
        """
    if name in self._internal_names_set or name in self._metadata or name in self._accessors:
        return object.__getattribute__(self, name)
    else:
        if self._info_axis._can_hold_identifiers_and_holds_name(name):
            return self[name]
        return object.__getattribute__(self, name)