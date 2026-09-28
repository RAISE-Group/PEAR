def _read_group(self, group: 'Node'):
    s = self._create_storer(group)
    s.infer_axes()
    return s.read()