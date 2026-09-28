def _set_formats_and_types(self, dtypes):
    self.typlist = []
    self.fmtlist = []
    for col, dtype in dtypes.items():
        self.fmtlist.append(_dtype_to_default_stata_fmt(dtype, self.data[col]))
        self.typlist.append(_dtype_to_stata_type(dtype, self.data[col]))