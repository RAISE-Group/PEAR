@cache_readonly
def indexables(self):
    """ create/cache the indexables if they don't exist """
    _indexables = []
    desc = self.description
    table_attrs = self.table.attrs
    for i, (axis, name) in enumerate(self.attrs.index_cols):
        atom = getattr(desc, name)
        md = self.read_metadata(name)
        meta = 'category' if md is not None else None
        kind_attr = f'{name}_kind'
        kind = getattr(table_attrs, kind_attr, None)
        index_col = IndexCol(name=name, axis=axis, pos=i, kind=kind, typ=atom, table=self.table, meta=meta, metadata=md)
        _indexables.append(index_col)
    dc = set(self.data_columns)
    base_pos = len(_indexables)

    def f(i, c):
        assert isinstance(c, str)
        klass = DataCol
        if c in dc:
            klass = DataIndexableCol
        atom = getattr(desc, c)
        adj_name = _maybe_adjust_name(c, self.version)
        values = getattr(table_attrs, f'{adj_name}_kind', None)
        dtype = getattr(table_attrs, f'{adj_name}_dtype', None)
        kind = _dtype_to_kind(dtype)
        md = self.read_metadata(c)
        meta = getattr(table_attrs, f'{adj_name}_meta', None)
        obj = klass(name=adj_name, cname=c, values=values, kind=kind, pos=base_pos + i, typ=atom, table=self.table, meta=meta, metadata=md, dtype=dtype)
        return obj
    _indexables.extend([f(i, c) for i, c in enumerate(self.attrs.values_cols)])
    return _indexables