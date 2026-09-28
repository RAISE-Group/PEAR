def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None):
    df = super().read(where=where, columns=columns, start=start, stop=stop)
    df = df.set_index(self.levels)
    df.index = df.index.set_names([None if self._re_levels.search(l) else l for l in df.index.names])
    return df