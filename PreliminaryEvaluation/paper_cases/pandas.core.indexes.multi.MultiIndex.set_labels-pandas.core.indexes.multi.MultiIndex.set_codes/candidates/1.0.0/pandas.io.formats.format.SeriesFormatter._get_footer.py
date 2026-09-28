def _get_footer(self) -> str:
    name = self.series.name
    footer = ''
    if getattr(self.series.index, 'freq', None) is not None:
        footer += 'Freq: {freq}'.format(freq=self.series.index.freqstr)
    if self.name is not False and name is not None:
        if footer:
            footer += ', '
        series_name = pprint_thing(name, escape_chars=('\t', '\r', '\n'))
        footer += 'Name: {sname}'.format(sname=series_name) if name is not None else ''
    if self.length is True or (self.length == 'truncate' and self.truncate_v):
        if footer:
            footer += ', '
        footer += 'Length: {length}'.format(length=len(self.series))
    if self.dtype is not False and self.dtype is not None:
        name = getattr(self.tr_series.dtype, 'name', None)
        if name:
            if footer:
                footer += ', '
            footer += 'dtype: {typ}'.format(typ=pprint_thing(name))
    if is_categorical_dtype(self.tr_series.dtype):
        level_info = self.tr_series._values._repr_categories_info()
        if footer:
            footer += '\n'
        footer += level_info
    return str(footer)