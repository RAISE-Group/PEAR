def _import_deprmod(self, mod=None):
    if mod is None:
        mod = self.deprmod
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=FutureWarning)
        deprmodule = importlib.import_module(mod)
        return deprmodule