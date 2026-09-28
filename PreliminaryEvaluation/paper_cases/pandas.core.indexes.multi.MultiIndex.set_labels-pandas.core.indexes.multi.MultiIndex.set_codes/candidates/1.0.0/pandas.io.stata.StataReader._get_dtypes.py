def _get_dtypes(self, seek_vartypes):
    self.path_or_buf.seek(seek_vartypes)
    raw_typlist = [struct.unpack(self.byteorder + 'H', self.path_or_buf.read(2))[0] for i in range(self.nvar)]

    def f(typ):
        if typ <= 2045:
            return typ
        try:
            return self.TYPE_MAP_XML[typ]
        except KeyError:
            raise ValueError(f'cannot convert stata types [{typ}]')
    typlist = [f(x) for x in raw_typlist]

    def f(typ):
        if typ <= 2045:
            return str(typ)
        try:
            return self.DTYPE_MAP_XML[typ]
        except KeyError:
            raise ValueError(f'cannot convert stata dtype [{typ}]')
    dtyplist = [f(x) for x in raw_typlist]
    return (typlist, dtyplist)