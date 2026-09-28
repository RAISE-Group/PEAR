def __setitem__(self, key: _KT, value: _VT) -> None:
    for mapping in self.maps:
        mutable_mapping = cast(MutableMapping[_KT, _VT], mapping)
        if key in mutable_mapping:
            mutable_mapping[key] = value
            return
    cast(MutableMapping[_KT, _VT], self.maps[0])[key] = value