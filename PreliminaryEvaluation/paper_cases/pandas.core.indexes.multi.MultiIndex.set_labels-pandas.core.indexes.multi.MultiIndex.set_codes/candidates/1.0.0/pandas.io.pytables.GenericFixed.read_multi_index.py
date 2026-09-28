def read_multi_index(self, key: str, start: Optional[int]=None, stop: Optional[int]=None) -> MultiIndex:
    nlevels = getattr(self.attrs, f'{key}_nlevels')
    levels = []
    codes = []
    names: List[Optional[Hashable]] = []
    for i in range(nlevels):
        level_key = f'{key}_level{i}'
        node = getattr(self.group, level_key)
        lev = self.read_index_node(node, start=start, stop=stop)
        levels.append(lev)
        names.append(lev.name)
        label_key = f'{key}_label{i}'
        level_codes = self.read_array(label_key, start=start, stop=stop)
        codes.append(level_codes)
    return MultiIndex(levels=levels, codes=codes, names=names, verify_integrity=True)