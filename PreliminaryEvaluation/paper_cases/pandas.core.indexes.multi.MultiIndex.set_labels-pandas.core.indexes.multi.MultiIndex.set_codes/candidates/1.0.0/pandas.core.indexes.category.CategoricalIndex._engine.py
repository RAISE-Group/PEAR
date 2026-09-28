@cache_readonly
def _engine(self):
    codes = self.codes
    return self._engine_type(lambda: codes, len(self))