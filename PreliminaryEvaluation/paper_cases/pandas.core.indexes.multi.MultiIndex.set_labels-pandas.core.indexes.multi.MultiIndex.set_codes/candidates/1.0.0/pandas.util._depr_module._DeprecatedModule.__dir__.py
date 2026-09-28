def __dir__(self) -> Iterable[str]:
    deprmodule = self._import_deprmod()
    return dir(deprmodule)