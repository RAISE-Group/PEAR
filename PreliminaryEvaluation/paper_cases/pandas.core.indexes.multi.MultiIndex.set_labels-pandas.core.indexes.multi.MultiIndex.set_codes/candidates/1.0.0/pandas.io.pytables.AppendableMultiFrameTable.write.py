def write(self, obj, data_columns=None, **kwargs):
    if data_columns is None:
        data_columns = []
    elif data_columns is True:
        data_columns = obj.columns.tolist()
    obj, self.levels = self.validate_multiindex(obj)
    for n in self.levels:
        if n not in data_columns:
            data_columns.insert(0, n)
    return super().write(obj=obj, data_columns=data_columns, **kwargs)