def _alias_to_class(self, alias):
    if isinstance(alias, type):
        return alias
    return self._reverse_index_map.get(alias, Index)