def _parse_numpy(self):
    load_kwargs = {'dtype': None, 'numpy': True, 'precise_float': self.precise_float}
    if self.orient in ['columns', 'index']:
        load_kwargs['labelled'] = True
    loads_ = functools.partial(loads, **load_kwargs)
    data = loads_(self.json)
    if self.orient == 'split':
        decoded = {str(k): v for k, v in data.items()}
        self.check_keys_split(decoded)
        self.obj = create_series_with_explicit_dtype(**decoded)
    elif self.orient in ['columns', 'index']:
        self.obj = create_series_with_explicit_dtype(*data, dtype_if_empty=object)
    else:
        self.obj = create_series_with_explicit_dtype(data, dtype_if_empty=object)