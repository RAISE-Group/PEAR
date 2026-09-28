def __setstate__(self, state: MutableMapping[str_type, Any]) -> None:
    self._categories = state.pop('categories', None)
    self._ordered = state.pop('ordered', False)