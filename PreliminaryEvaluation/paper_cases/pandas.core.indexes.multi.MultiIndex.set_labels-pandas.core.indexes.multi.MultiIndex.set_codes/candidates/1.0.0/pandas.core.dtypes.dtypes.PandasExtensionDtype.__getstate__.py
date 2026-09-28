def __getstate__(self) -> Dict[str_type, Any]:
    return {k: getattr(self, k, None) for k in self._metadata}