def _class_to_alias(self, cls) -> str:
    return self._index_type_map.get(cls, '')