def __delitem__(self, key: _KT) -> None:
    """
        Raises
        ------
        KeyError
            If `key` doesn't exist.
        """
    for mapping in self.maps:
        mutable_mapping = cast(MutableMapping[_KT, _VT], mapping)
        if key in mapping:
            del mutable_mapping[key]
            return
    raise KeyError(key)