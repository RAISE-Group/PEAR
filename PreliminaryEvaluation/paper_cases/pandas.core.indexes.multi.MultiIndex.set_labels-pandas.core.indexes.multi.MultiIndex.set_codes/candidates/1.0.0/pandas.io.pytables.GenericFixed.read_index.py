def read_index(self, key: str, start: Optional[int]=None, stop: Optional[int]=None) -> Index:
    variety = _ensure_decoded(getattr(self.attrs, f'{key}_variety'))
    if variety == 'multi':
        return self.read_multi_index(key, start=start, stop=stop)
    elif variety == 'regular':
        node = getattr(self.group, key)
        index = self.read_index_node(node, start=start, stop=stop)
        return index
    else:
        raise TypeError(f'unrecognized index variety: {variety}')