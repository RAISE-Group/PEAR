@property
def _hasna(self) -> bool:
    return self._mask.any()