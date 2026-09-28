def __getattr__(self, name: str):
    if name in self.self_dir:
        return object.__getattribute__(self, name)
    try:
        deprmodule = self._import_deprmod(self.deprmod)
    except ImportError:
        if self.deprmodto is None:
            raise
        deprmodule = self._import_deprmod(self.deprmodto)
    obj = getattr(deprmodule, name)
    if self.removals is not None and name in self.removals:
        warnings.warn(f'{self.deprmod}.{name} is deprecated and will be removed in a future version.', FutureWarning, stacklevel=2)
    elif self.moved is not None and name in self.moved:
        warnings.warn(f'{self.deprmod} is deprecated and will be removed in a future version.\nYou can access {name} as {self.moved[name]}', FutureWarning, stacklevel=2)
    else:
        deprmodto = self.deprmodto
        if deprmodto is False:
            warnings.warn(f'{self.deprmod}.{name} is deprecated and will be removed in a future version.', FutureWarning, stacklevel=2)
        else:
            if deprmodto is None:
                deprmodto = obj.__module__
            warnings.warn(f'{self.deprmod}.{name} is deprecated. Please use {deprmodto}.{name} instead.', FutureWarning, stacklevel=2)
    return obj