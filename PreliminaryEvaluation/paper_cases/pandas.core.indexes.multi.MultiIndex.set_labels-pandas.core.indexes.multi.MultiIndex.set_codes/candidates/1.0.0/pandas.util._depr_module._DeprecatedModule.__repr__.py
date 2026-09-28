def __repr__(self) -> str:
    deprmodule = self._import_deprmod()
    return repr(deprmodule)