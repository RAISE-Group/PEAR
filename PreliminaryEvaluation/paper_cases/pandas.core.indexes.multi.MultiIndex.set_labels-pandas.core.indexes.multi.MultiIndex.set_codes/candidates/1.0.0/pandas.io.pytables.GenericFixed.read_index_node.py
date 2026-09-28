def read_index_node(self, node: 'Node', start: Optional[int]=None, stop: Optional[int]=None) -> Index:
    data = node[start:stop]
    if 'shape' in node._v_attrs and np.prod(node._v_attrs.shape) == 0:
        data = np.empty(node._v_attrs.shape, dtype=node._v_attrs.value_type)
    kind = _ensure_decoded(node._v_attrs.kind)
    name = None
    if 'name' in node._v_attrs:
        name = _ensure_str(node._v_attrs.name)
        name = _ensure_decoded(name)
    index_class = self._alias_to_class(_ensure_decoded(getattr(node._v_attrs, 'index_class', '')))
    factory = self._get_index_factory(index_class)
    kwargs = {}
    if 'freq' in node._v_attrs:
        kwargs['freq'] = node._v_attrs['freq']
    if 'tz' in node._v_attrs:
        if isinstance(node._v_attrs['tz'], bytes):
            kwargs['tz'] = node._v_attrs['tz'].decode('utf-8')
        else:
            kwargs['tz'] = node._v_attrs['tz']
    if kind == 'date':
        index = factory(_unconvert_index(data, kind, encoding=self.encoding, errors=self.errors), dtype=object, **kwargs)
    else:
        index = factory(_unconvert_index(data, kind, encoding=self.encoding, errors=self.errors), **kwargs)
    index.name = name
    return index