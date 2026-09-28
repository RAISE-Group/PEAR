def read(self, where=None, columns=None, start: Optional[int]=None, stop: Optional[int]=None) -> Series:
    is_multi_index = self.is_multi_index
    if columns is not None and is_multi_index:
        assert isinstance(self.levels, list)
        for n in self.levels:
            if n not in columns:
                columns.insert(0, n)
    s = super().read(where=where, columns=columns, start=start, stop=stop)
    if is_multi_index:
        s.set_index(self.levels, inplace=True)
    s = s.iloc[:, 0]
    if s.name == 'values':
        s.name = None
    return s