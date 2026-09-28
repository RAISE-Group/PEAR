def validate(self, other):
    """ validate against an existing table """
    if other is None:
        return
    if other.table_type != self.table_type:
        raise TypeError(f'incompatible table_type with existing [{other.table_type} - {self.table_type}]')
    for c in ['index_axes', 'non_index_axes', 'values_axes']:
        sv = getattr(self, c, None)
        ov = getattr(other, c, None)
        if sv != ov:
            for i, sax in enumerate(sv):
                oax = ov[i]
                if sax != oax:
                    raise ValueError(f'invalid combination of [{c}] on appending data [{sax}] vs current table [{oax}]')
            raise Exception(f'invalid combination of [{c}] on appending data [{sv}] vs current table [{ov}]')