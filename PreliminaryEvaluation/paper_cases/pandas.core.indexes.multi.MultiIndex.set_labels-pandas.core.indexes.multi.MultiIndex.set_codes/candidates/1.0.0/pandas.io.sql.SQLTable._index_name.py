def _index_name(self, index, index_label):
    if index is True:
        nlevels = self.frame.index.nlevels
        if index_label is not None:
            if not isinstance(index_label, list):
                index_label = [index_label]
            if len(index_label) != nlevels:
                raise ValueError(f"Length of 'index_label' should match number of levels, which is {nlevels}")
            else:
                return index_label
        if nlevels == 1 and 'index' not in self.frame.columns and (self.frame.index.name is None):
            return ['index']
        else:
            return [l if l is not None else f'level_{i}' for i, l in enumerate(self.frame.index.names)]
    elif isinstance(index, str):
        return [index]
    elif isinstance(index, list):
        return index
    else:
        return None