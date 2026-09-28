def write(self, obj, axes=None, append=False, complib=None, complevel=None, fletcher32=None, min_itemsize=None, chunksize=None, expectedrows=None, dropna=False, nan_rep=None, data_columns=None):
    if not append and self.is_exists:
        self._handle.remove_node(self.group, 'table')
    table = self._create_axes(axes=axes, obj=obj, validate=append, min_itemsize=min_itemsize, nan_rep=nan_rep, data_columns=data_columns)
    for a in table.axes:
        a.validate_names()
    if not table.is_exists:
        options = table.create_description(complib=complib, complevel=complevel, fletcher32=fletcher32, expectedrows=expectedrows)
        table.set_attrs()
        table._handle.create_table(table.group, **options)
    table.attrs.info = table.info
    for a in table.axes:
        a.validate_and_set(table, append)
    table.write_data(chunksize, dropna=dropna)